import base64
import json
import re
import hashlib
import hmac
from jsonview.decorators import json_view
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render, redirect

from django.utils.safestring import mark_safe
from django.conf import settings
from django.http import Http404, HttpResponse
from django.contrib import messages
from django.template import loader, Context
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
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
    print(data)




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
    errors = ""
    data = request.POST.get('form', '')
    form = {}
    data = json.loads(data)

    for i in data:
        form[i['name']] = i['value']

    if form['customer_name']:
        if len(form['customer_name']) >= 1:
            this_order.name = form['customer_name']
    else:
        errors += "Print your name <br>"
    if 'customer_surname' in form:
        if len(form['customer_surname']) >= 1:
            this_order.last_name = form['customer_surname']
    else:
        errors += "Print your surname <br>"
    if 'customer_phone' in form:
        if len(form['customer_phone']) >= 1:
            this_order.phone = form['customer_phone']
    else:
        errors += "Print your phone <br>"
    if 'customer_email' in form:
        if not re.match(r'[^@]+@[^@]+\.[^@]+', form['customer_email']):
            errors += "Print correct email <br>"
        if len(form['customer_email']) >= 1:
            this_order.email = form['customer_email']
    else:
        errors += "Print your email <br>"

    if 'ordr-deliv-worldwide' in form:
        if form['ordr-deliv-worldwide'] == 'on':
            this_order.delivery_method = 'Worldwide'
            if 'order-delivery-country-world-wide' in form:
                if len(form['order-delivery-country-world-wide']) >= 1:
                    this_order.comment += form['order-delivery-country-world-wide']
                    this_order.comment += '\n'
                else:
                    errors += 'Print country to deliver <br>'
            if 'order-delivery-region-world-wide' in form:
                if len(form['order-delivery-region-world-wide']) >= 1:
                    this_order.comment += form['order-delivery-region-world-wide']
                    this_order.comment += '\n'
                else:
                    errors += 'Print region to deliver <br>'
            if 'order-delivery-city-world-wide' in form:
                if len(form['order-delivery-city-world-wide']) >= 1:
                    this_order.comment += form['order-delivery-city-world-wide']
                    this_order.comment += '\n'
                else:
                    errors += 'Print city to deliver <br>'
            if 'order-delivery-street-world-wide' in form:
                if len(form['order-delivery-street-world-wide']) >= 1:
                    this_order.comment += form['order-delivery-street-world-wide']
                    this_order.comment += '\n'
                else:
                    errors += 'Print street to deliver <br>'
            if 'order-delivery-building-world-wide' in form:
                if len(form['order-delivery-building-world-wide']) >= 1:
                    this_order.comment += form['order-delivery-building-world-wide']
                    this_order.comment += '\n'
                else:
                    errors += 'Print building number <br>'
            if 'order-delivery-apartment-world-wide' in form:
                if len(form['order-delivery-apartment-world-wide']) >= 1:
                    this_order.comment += form['order-delivery-apartment-world-wide']
                    this_order.comment += '\n'
                else:
                    errors += 'Print apartment number <br>'
            if 'order-delivery-zipcode-world-wide' in form:
                if len(form['order-delivery-zipcode-world-wide']) >= 1:
                    this_order.comment += form['order-delivery-zipcode-world-wide']
                    this_order.comment += '\n'
                else:
                    errors += 'Print zipcode <br>'

    elif 'ordr-deliv-novpostobranch' in form:
        if form['ordr-deliv-novpostobranch'] == 'on':
            this_order.delivery_method = 'Nova Posta to branch'
            if 'order-delivery-region-np-to-branch' in form:
                if len(form['order-delivery-region-np-to-branch']) >= 1:
                    this_order.comment += form['order-delivery-region-np-to-branch']
                    this_order.comment += '\n'
                else:
                    errors += 'Print region to deliver <br>'
            if 'order-delivery-city-np-to-branch' in form:
                if len(form['order-delivery-city-np-to-branch']) >= 1:
                    this_order.comment += form['order-delivery-city-np-to-branch']
                    this_order.comment += '\n'
                else:
                    errors += 'Print city <br>'
            if 'order-delivery-office-np-to-branch' in form:
                if len(form['order-delivery-office-np-to-branch']) >= 1:
                    this_order.comment += form['order-delivery-office-np-to-branch']
                    this_order.comment += '\n'
                else:
                    errors += 'Print office number <br>'

    elif 'ordr-deliv-novpostodoor' in form:
        if form['ordr-deliv-novpostodoor'] == 'on':
            this_order.delivery_method = 'Nova Posta to door'
            if 'order-delivery-region-np-to-door' in form:
                if len(form['order-delivery-region-np-to-door']) >= 1:
                    this_order.comment += form['order-delivery-region-np-to-door']
                    this_order.comment += '\n'
                else:
                    errors += 'Print region <br>'
            if 'order-delivery-city-np-to-door' in form:
                if len(form['order-delivery-city-np-to-door']) >= 1:
                    this_order.comment += form['order-delivery-city-np-to-door']
                    this_order.comment += '\n'
                else:
                    errors += 'Print city <br>'
            if 'order-delivery-street-np-to-door' in form:
                if len(form['order-delivery-street-np-to-door']) >= 1:
                    this_order.comment += form['order-delivery-street-np-to-door']
                    this_order.comment += '\n'
                else:
                    errors += 'Print street <br>'
            if 'order-delivery-building-np-to-door' in form:
                if len(form['order-delivery-building-np-to-door']) >= 1:
                    this_order.comment += form['order-delivery-building-np-to-door']
                    this_order.comment += '\n'
                else:
                    errors += 'Print street <br>'
            if 'order-delivery-building-np-to-door' in form:
                if len(form['order-delivery-building-np-to-door']) >= 1:
                    this_order.comment += form['order-delivery-building-np-to-door']
                    this_order.comment += '\n'
                else:
                    errors += 'Print building number <br>'
            if 'order-delivery-apartment-np-to-door' in form:
                if len(form['order-delivery-apartment-np-to-door']) >= 1:
                    this_order.comment += form['order-delivery-apartment-np-to-door']
                    this_order.comment += '\n'
                else:
                    errors += 'Print apartment number <br>'

    elif 'ordr-deliv-urkpostobranch' in form:
        if form['ordr-deliv-urkpostobranch'] == 'on':
            this_order.delivery_method = 'Ukr Posta to branch'
            if 'order-delivery-region-ukrp-to-branch' in form:
                if len(form['order-delivery-region-ukrp-to-branch']) >= 1:
                    this_order.comment += form['order-delivery-region-ukrp-to-branch']
                    this_order.comment += '\n'
                else:
                    errors += 'Print region <br>'
        if form['ordr-deliv-urkpostobranch'] == 'on':
            if 'order-delivery-city-ukrp-to-branch' in form:
                if len(form['order-delivery-city-ukrp-to-branch']) >= 1:
                    this_order.comment += form['order-delivery-city-ukrp-to-branch']
                    this_order.comment += '\n'
                else:
                    errors += 'Print city <br>'
            if 'order-delivery-office-ukrp-to-branch' in form:
                if len(form['order-delivery-office-ukrp-to-branch']) >= 1:
                    this_order.comment += form['order-delivery-office-ukrp-to-branch']
                    this_order.comment += '\n'
                else:
                    errors += 'Print office number <br>'

    elif 'ordr-deliv-urkpostodoor' in form:
        if form['ordr-deliv-urkpostodoor'] == 'on':
            this_order.delivery_method = 'Ukr Posta to door'
            if 'order-delivery-region-ukrp-to-door' in form:
                if len(form['order-delivery-region-ukrp-to-door']) >= 1:
                    this_order.comment += form['order-delivery-region-ukrp-to-door']
                    this_order.comment += '\n'
                else:
                    errors += 'Print region <br>'
            if 'order-delivery-city-ukrp-to-door' in form:
                if len(form['order-delivery-city-ukrp-to-door']) >= 1:
                    this_order.comment += form['order-delivery-city-ukrp-to-door']
                    this_order.comment += '\n'
                else:
                    errors += 'Print city <br>'
            if 'order-delivery-street-ukrp-to-door' in form:
                if len(form['order-delivery-street-ukrp-to-door']) >= 1:
                    this_order.comment += form['order-delivery-street-ukrp-to-door']
                    this_order.comment += '\n'
                else:
                    errors += 'Print street <br>'
            if 'order-delivery-building-ukrp-to-door' in form:
                if len(form['order-delivery-building-ukrp-to-door']) >= 1:
                    this_order.comment += form['order-delivery-building-ukrp-to-door']
                    this_order.comment += '\n'
                else:
                    errors += 'Print building number <br>'
            if 'order-delivery-apartment-ukrp-to-door' in form:
                if len(form['order-delivery-apartment-ukrp-to-door']) >= 1:
                    this_order.comment += form['order-delivery-apartment-ukrp-to-door']
                    this_order.comment += '\n'
                else:
                    errors += 'Print apartment number <br>'
            if 'order-delivery-zipcode-ukrp-to-door' in form:
                if len(form['order-delivery-zipcode-ukrp-to-door']) >= 1:
                    this_order.comment += form['order-delivery-zipcode-ukrp-to-door']
                    this_order.comment += '\n'
                else:
                    errors += 'Print zipcode <br>'

    elif 'ordr-deliv-justintobranch' in form:
        if form['ordr-deliv-justintobranch'] == 'on':
            this_order.delivery_method = 'Justin to branch'
            if 'order-delivery-region-justin-to-branch' in form:
                if len(form['order-delivery-region-justin-to-branch']) >= 1:
                    this_order.comment += form['order-delivery-region-justin-to-branch']
                    this_order.comment += '\n'
                else:
                    errors += 'Print region <br>'
            if 'order-delivery-city-justin-to-branch' in form:
                if len(form['order-delivery-city-justin-to-branch']) >= 1:
                    this_order.comment += form['order-delivery-city-justin-to-branch']
                    this_order.comment += '\n'
                else:
                    errors += 'Print region <br>'
            if 'order-delivery-office-justin-to-branch' in form:
                if len(form['order-delivery-office-justin-to-branch']) >= 1:
                    this_order.comment += form['order-delivery-office-justin-to-branch']
                    this_order.comment += '\n'
                else:
                    errors += 'Print office number <br>'
    else:
        errors += 'Choose delivery type <br>'

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
        errors += 'Chose payment type <br>'

    if errors == "":
        this_order.save()
        cart = get_object_or_404(Cart, session_key=request.session.session_key)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            item.delete()
        cart_amount = 0
        return {'success': True, 'cart_amount': cart_amount}

    errors_block = '<div class="row"><a  id="errors" class="btn btn-warning btn-lg rounded-0 mt-4 mb-0 mx-auto disabled" ' \
                   'style="font-size:8px height:auto; width:auto;">' + errors + '</a></div>'
    errors_block = mark_safe(errors_block)
    print('\n\n\n', errors_block, '\n\n\n')
    return {'success': False, "errors": errors_block}





