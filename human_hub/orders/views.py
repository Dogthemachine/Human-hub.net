import json
import re
import hashlib
import hmac
from jsonview.decorators import json_view
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.safestring import mark_safe
from django.conf import settings
from django.http import Http404, HttpResponse
from django.template import loader, Context
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.utils.dateformat import format

from showcase.models import Photo, Categories, Items, Sizes, Balance, Config
from orders.models import Orders, OrderItems, Payment, PaymentRaw, Cart, CartItem


@json_view
def cart(request):
    cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    cart.session = request.session.session_key
    cart.save()
    tot_price = 0
    if not created:
        cart_items = CartItem.objects.filter(cart=cart)
        for c_i in cart_items:
            c_i.bal = Balance.objects.get(item=c_i.item, size=c_i.size).amount
            tot_price += c_i.item.price
    else:
        cart_items = []
    t = loader.get_template('orders/cart.html')
    c = {'cart': cart, 'cart_items': cart_items, 'total_price': tot_price}
    html = t.render(c, request)

    return {'html': html}


@json_view
def order(request):
    cart = get_object_or_404(Cart, session_key=request.session.session_key)
    tot_price = 0
    cart_items = CartItem.objects.filter(cart=cart)
    for c_i in cart_items:
        c_i.bal = Balance.objects.get(item=c_i.item, size=c_i.size).amount
        tot_price += c_i.item.price
    t = loader.get_template('orders/make_order.html')
    html = t.render({'total_price': tot_price}, request)

    return {'html': html}

@json_view
def submit(request, data):
    pass


@csrf_exempt
@json_view
def cart_remove(request, id):
    cart_item = get_object_or_404(CartItem, id=id)
    cart_item.delete()
    request.cart_amount -= 1
    cart_total = cart_item.cart.get_total()

    return {'success': True, 'cart_amount': request.cart_amount, 'cart_total': cart_total}


@csrf_exempt
@json_view
def cart_add(request, id, size_id):

    if size_id:
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
        item = get_object_or_404(Items, id=id)
        size = get_object_or_404(Sizes, id=size_id)
        cart_item = CartItem(cart=cart, item=item, size=size, amount=1)
        cart_item.save()
        request.cart_amount += 1

        return {'success': True, 'cart_amount': request.cart_amount}

    return {'success': False}


def price_description(request):
    config = Config.objects.get()
    description = ''
    if request.session['valuta']=='grn':
        description = config.price_description
    if request.session['valuta']=='usd':
        description = config.price_description_usd
    if request.session['valuta']=='eur':
        description = config.price_description_eur

    return description

def normalize_phone(phone):
    phone = "".join(i for i in phone if i.isdigit())
    if len(phone) == 10:
        phone = "38" + phone
    elif len(phone) == 9:
        phone = "380" + phone
    else:
        pass
    if len(phone) == 0:
        phone = 0

    return phone


@csrf_exempt
@json_view
def cart_checkout(request):
    this_order = Orders()

#   ------- ORDER FORM VALIDATION --------
    errors = ""
    data = request.POST.get('form', '')
    form = {l['name']: l['value'] for l in json.loads(data)}

    if 'customer_name' in form:
        if len(form['customer_name']) >= 1:
            this_order.name = form['customer_name']
        else:
            errors += _("Print your name") + "<br>"
    if 'customer_surname' in form:
        if len(form['customer_surname']) >= 1:
            this_order.last_name = form['customer_surname']
        else:
            errors += _("Print your surname") + "<br>"
    if 'customer_phone' in form:
        if len(form['customer_phone']) >= 1:
            this_order.phone = form['customer_phone']
        else:
            errors += _("Print your phone") + "<br>"
    if 'customer_email' in form:
        if len(form['customer_email']) >= 1:
            if not re.match(r'[^@]+@[^@]+\.[^@]+', form['customer_email']):
                errors += _("Print correct email") + "<br>"
            this_order.email = form['customer_email']
        else:
            errors += _("Print your email") + "<br>"
    if 'ordr-deliv-worldwide' in form:
        if form['ordr-deliv-worldwide'] == 'on':
            this_order.delivery_method = 'Worldwide'
            if 'order-delivery-country-world-wide' in form:
                if len(form['order-delivery-country-world-wide']) >= 1:
                    this_order.comment += _('country ')
                    this_order.comment += form['order-delivery-country-world-wide']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print country to deliver") + "<br>"
            if 'order-delivery-region-world-wide' in form:
                if len(form['order-delivery-region-world-wide']) >= 1:
                    this_order.comment += _('region ')
                    this_order.comment += form['order-delivery-region-world-wide']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print region to deliver") + "<br>"
            if 'order-delivery-city-world-wide' in form:
                if len(form['order-delivery-city-world-wide']) >= 1:
                    this_order.comment += _('city ')
                    this_order.comment += form['order-delivery-city-world-wide']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print city to deliver") + "<br>"
            if 'order-delivery-street-world-wide' in form:
                if len(form['order-delivery-street-world-wide']) >= 1:
                    this_order.comment += _('street ')
                    this_order.comment += form['order-delivery-street-world-wide']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print street to deliver") + "<br>"
            if 'order-delivery-building-world-wide' in form:
                if len(form['order-delivery-building-world-wide']) >= 1:
                    this_order.comment += _('building ')
                    this_order.comment += form['order-delivery-building-world-wide']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print building number") + "<br>"
            if 'order-delivery-apartment-world-wide' in form:
                if len(form['order-delivery-apartment-world-wide']) >= 1:
                    this_order.comment += _('apartment ')
                    this_order.comment += form['order-delivery-apartment-world-wide']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print apartment number") + "<br>"
            if 'order-delivery-zipcode-world-wide' in form:
                if len(form['order-delivery-zipcode-world-wide']) >= 1:
                    this_order.comment += _('zipcode ')
                    this_order.comment += form['order-delivery-zipcode-world-wide']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print zipcode") + "<br>"
    elif 'ordr-deliv-novpostobranch' in form:
        if form['ordr-deliv-novpostobranch'] == 'on':
            this_order.delivery_method = 'Nova Posta to branch'
            if 'order-delivery-region-np-to-branch' in form:
                if len(form['order-delivery-region-np-to-branch']) >= 1:
                    this_order.comment += _('region ')
                    this_order.comment += form['order-delivery-region-np-to-branch']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print region to deliver") + "<br>"
            if 'order-delivery-city-np-to-branch' in form:
                if len(form['order-delivery-city-np-to-branch']) >= 1:
                    this_order.comment += _('city ')
                    this_order.comment += form['order-delivery-city-np-to-branch']
                    this_order.comment += '/p'
                else:
                    errors += _("Print city") + "<br>"
            if 'order-delivery-office-np-to-branch' in form:
                if len(form['order-delivery-office-np-to-branch']) >= 1:
                    this_order.comment += _('office ')
                    this_order.comment += form['order-delivery-office-np-to-branch']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print office number") + "<br>"
    elif 'ordr-deliv-novpostodoor' in form:
        if form['ordr-deliv-novpostodoor'] == 'on':
            this_order.delivery_method = 'Nova Posta to door'
            if 'order-delivery-region-np-to-door' in form:
                if len(form['order-delivery-region-np-to-door']) >= 1:
                    this_order.comment += _('region ')
                    this_order.comment += form['order-delivery-region-np-to-door']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print region") + "<br>"
            if 'order-delivery-city-np-to-door' in form:
                if len(form['order-delivery-city-np-to-door']) >= 1:
                    this_order.comment += _('city ')
                    this_order.comment += form['order-delivery-city-np-to-door']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print city") + "<br>"
            if 'order-delivery-street-np-to-door' in form:
                if len(form['order-delivery-street-np-to-door']) >= 1:
                    this_order.comment += _('street ')
                    this_order.comment += form['order-delivery-street-np-to-door']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print street") + "<br>"
            if 'order-delivery-building-np-to-door' in form:
                if len(form['order-delivery-building-np-to-door']) >= 1:
                    this_order.comment += _('building ')
                    this_order.comment += form['order-delivery-building-np-to-door']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print street") + "<br>"
            if 'order-delivery-building-np-to-door' in form:
                if len(form['order-delivery-building-np-to-door']) >= 1:
                    this_order.comment += _('building ')
                    this_order.comment += form['order-delivery-building-np-to-door']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print building number") +"<br>"
            if 'order-delivery-apartment-np-to-door' in form:
                if len(form['order-delivery-apartment-np-to-door']) >= 1:
                    this_order.comment += _('apartment ')
                    this_order.comment += form['order-delivery-apartment-np-to-door']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print apartment number") + "<br>"
    elif 'ordr-deliv-urkpostobranch' in form:
        if form['ordr-deliv-urkpostobranch'] == 'on':
            this_order.delivery_method = 'Ukr Posta to branch'
            if 'order-delivery-region-ukrp-to-branch' in form:
                if len(form['order-delivery-region-ukrp-to-branch']) >= 1:
                    this_order.comment += _('region ')
                    this_order.comment += form['order-delivery-region-ukrp-to-branch']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print region") + "<br>"
        if form['ordr-deliv-urkpostobranch'] == 'on':
            if 'order-delivery-city-ukrp-to-branch' in form:
                if len(form['order-delivery-city-ukrp-to-branch']) >= 1:
                    this_order.comment += _('city ')
                    this_order.comment += form['order-delivery-city-ukrp-to-branch']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print city") + "<br>"
            if 'order-delivery-office-ukrp-to-branch' in form:
                if len(form['order-delivery-office-ukrp-to-branch']) >= 1:
                    this_order.comment += _('office ')
                    this_order.comment += form['order-delivery-office-ukrp-to-branch']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print office number") + "<br>"
    elif 'ordr-deliv-urkpostodoor' in form:
        if form['ordr-deliv-urkpostodoor'] == 'on':
            this_order.delivery_method = 'Ukr Posta to door'
            if 'order-delivery-region-ukrp-to-door' in form:
                if len(form['order-delivery-region-ukrp-to-door']) >= 1:
                    this_order.comment += _('region ')
                    this_order.comment += form['order-delivery-region-ukrp-to-door']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print region") + "<br>"
            if 'order-delivery-city-ukrp-to-door' in form:
                if len(form['order-delivery-city-ukrp-to-door']) >= 1:
                    this_order.comment += _('city ')
                    this_order.comment += form['order-delivery-city-ukrp-to-door']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print city") + "<br>"
            if 'order-delivery-street-ukrp-to-door' in form:
                if len(form['order-delivery-street-ukrp-to-door']) >= 1:
                    this_order.comment += _('street ')
                    this_order.comment += form['order-delivery-street-ukrp-to-door']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print street") + "<br>"
            if 'order-delivery-building-ukrp-to-door' in form:
                if len(form['order-delivery-building-ukrp-to-door']) >= 1:
                    this_order.comment += _('building ')
                    this_order.comment += form['order-delivery-building-ukrp-to-door']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print building number") + "<br>"
            if 'order-delivery-apartment-ukrp-to-door' in form:
                if len(form['order-delivery-apartment-ukrp-to-door']) >= 1:
                    this_order.comment += form['order-delivery-apartment-ukrp-to-door']
                    this_order.comment += _('apartment ')
                    this_order.comment += '</p>'
                else:
                    errors += _("Print apartment number") + "<br>"
            if 'order-delivery-zipcode-ukrp-to-door' in form:
                if len(form['order-delivery-zipcode-ukrp-to-door']) >= 1:
                    this_order.comment += _('zipcode ')
                    this_order.comment += form['order-delivery-zipcode-ukrp-to-door']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print zipcode") + "<br>"
    elif 'ordr-deliv-justintobranch' in form:
        if form['ordr-deliv-justintobranch'] == 'on':

            this_order.delivery_method = 'Justin to branch'
            if 'order-delivery-region-justin-to-branch' in form:
                if len(form['order-delivery-region-justin-to-branch']) >= 1:
                    this_order.comment += _('region ')
                    this_order.comment += form['order-delivery-region-justin-to-branch']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print region") + "<br>"
            if 'order-delivery-city-justin-to-branch' in form:
                if len(form['order-delivery-city-justin-to-branch']) >= 1:
                    this_order.comment += _('city ')
                    this_order.comment += form['order-delivery-city-justin-to-branch']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print region") + "<br>"
            if 'order-delivery-office-justin-to-branch' in form:
                if len(form['order-delivery-office-justin-to-branch']) >= 1:
                    this_order.comment += _('office ')
                    this_order.comment += form['order-delivery-office-justin-to-branch']
                    this_order.comment += '</p>'
                else:
                    errors += _("Print office number") + "<br>"
    else:
        errors += _("Choose delivery type") + "<br>"
#   ------- ORDER FORM VALIDATION --------

    if 'ordr-pay-visa-mstrcrd' in form:
        if form['ordr-pay-visa-mstrcrd'] == 'on':
            this_order.payment_method = 'VisaMastercard'
    elif 'ordr-pay-applepay' in form:
        if form['ordr-pay-applepay'] == 'on':
            this_order.payment_method = 'ApplePay'
    elif 'ordr-pay-googlepay' in form:
        if form['ordr-pay-googlepay'] == 'on':
            this_order.payment_method = 'GooglePay'
    elif 'ordr-pay-paypal' in form:
        if form['ordr-pay-paypal'] == 'on':
            this_order.payment_method = 'PayPal'
    elif 'ordr-pay-bycard' in form:
        if form['ordr-pay-bycard'] == 'on':
            this_order.payment_method = 'ByCard'
    elif 'ordr-pay-cash-on-del' in form:
        if form['ordr-pay-cash-on-del'] == 'on':
            this_order.payment_method = 'CashOnDelivery'
    else:
        errors += _("Chose payment type") + "<br>"

    if errors == "":

        this_order.save()

#   ------- MAKING ORDER ITEMS --------
        cart = get_object_or_404(Cart, session_key=request.session.session_key)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            balance = get_object_or_404(Balance, item=item.item, size=item.size)
            balance.amount -= 1
            order_item = OrderItems(order=this_order, balance=balance, amount=1, price=item.item.price)
            order_item.save()
#   ------- MAKING ORDER ITEMS--------

        if this_order.payment_method in ('VisaMastercard', 'ApplePay', 'GooglePay', 'PayPal'):
            config = Config.objects.get()
            payment = {}

            payment['account'] = config.merchant_account
            payment['domain'] = config.merchant_domain_name
            payment['tr_type'] = 'SALE'
            payment['auth_type'] = 'SimpleSignature'
            payment['sign'] = ''
            payment['url'] = 'https://' + config.merchant_domain_name + 'wfp_callback/'
            payment['order_id'] = this_order.id
            payment['order_date'] = format(this_order.added, 'U')
            payment['amount'] = this_order.get_total_price_grn()
            payment['currency'] = 'UAH'
            payment['products'] = []
            payment['prices'] = []
            payment['counts'] = []
            payment['first_name'] = this_order.name
            payment['last_name'] = this_order.last_name
            payment['phone'] = this_order.phone
            payment['lang'] = 'AUTO'

            for order_item in this_order.orderitems_set.all():
                payment['products'].append(order_item.balance.item.name)
                payment['prices'].append(order_item.price)
                payment['counts'].append(order_item.amount)

            products_str = ';'.join(payment['products'])
            prices_str = ';'.join(str(x) for x in payment['prices'])
            counts_str = ';'.join(str(x) for x in payment['counts'])

            sign_str = ';'.join([
                payment['account'], payment['domain'], str(payment['order_id']),
                str(payment['order_date']), str(payment['amount']), payment['currency'],
                products_str, str(counts_str), str(prices_str)
            ])
            payment['sign'] = hmac.new(
                str.encode(config.merchant_secret),
                str.encode(sign_str),
                hashlib.md5
            ).hexdigest()

            return {'success': True, 'payment': payment}

        if this_order.payment_method == 'ByCard':
            message = _("Your order is accepted. Order number is ") + str(this_order.id) + "." + "<br>" \
                      + _("Cart number to pay is ") + "<br>"
            message += settings.PRIVAT_CARD
            info_block = '<div class="row"><a  id="errors" class="btn btn-lg made_order mt-4 mb-0 mx-auto disabled" ' \
                         'style="color:black; height:auto; width:auto;">' + message + '</a></div>'
            cart = get_object_or_404(Cart, session_key=request.session.session_key)
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                item.delete()
            cart_amount = 0

            return {'success': True, 'cart_amount': cart_amount, "info_block": info_block, }

        if this_order.payment_method == 'CashOnDelivery':
            message = _("Your order is accepted. Order number is ") + str(this_order.id) + "." + "<br>" \
                      + _("Our manager will contact you to clarify the details, if necessary")
            info_block = '<div class="row"><a  id="errors" class="btn btn-lg made_order mt-4 mb-0 mx-auto disabled" ' \
                         'style="color:black; height:auto; width:auto;">' + message + '</a></div>'
            cart = get_object_or_404(Cart, session_key=request.session.session_key)
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                item.delete()
            cart_amount = 0

            return {'success': True, 'cart_amount': cart_amount, "info_block": info_block,}



    info_block = '<div class="row"><a  id="errors" class="btn btn-lg choose_size_before mt-4 mb-0 mx-auto disabled" '\
                   'style="color:black; height:auto; width:auto;">' + errors + '</a></div>'
    info_block = mark_safe(info_block)

    return {'success': False, "info_block": info_block}


@csrf_exempt
def wfp_callback(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except:
            raise

        sign_str = ';'.join([
            data['merchantAccount'], str(data['orderReference']), str(data['amount']),
            data['currency'], str(data['authCode']), data['cardPan'],
            data['transactionStatus'], str(data['reasonCode'])
        ])

        sign = hmac.new(
            str.encode(settings.MERCHANT_SIGNATURE),
            str.encode(sign_str),
            hashlib.md5
        ).hexdigest()

        print('\n\n')
        print('---------wfp_callback---------')
        print(data)
        print('\n\n')

        if sign == data['merchantSignature']:
            response_dict = {}
            response_dict['orderReference'] = data['orderReference']
            response_dict['status'] = 'accept'
            response_dict['time'] = format(timezone.now(), 'U')
            response_dict['signature'] = ''

            response_sign_str = ';'.join([
                response_dict['orderReference'], response_dict['status'],
                str(response_dict['time'])
            ])

            response_dict['signature'] = hmac.new(
                str.encode(settings.MERCHANT_SIGNATURE),
                str.encode(response_sign_str),
                hashlib.md5
            ).hexdigest()

            print(data['transactionStatus'])

            if data['transactionStatus'] == 'Approved':
                print('---------wfp_callback---------')
                print('\n\n')

            return HttpResponse(json.dumps(response_dict, ensure_ascii=False), content_type="text/plain")

        else:
            print('>>>>>>>>>>wfp_callback>>>>>>>>>>')
            return HttpResponse()





