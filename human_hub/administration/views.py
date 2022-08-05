from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from orders.models import Orders, OrderItems, Payment
from django.utils.translation import gettext as _
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required, login_required

from jsonview.decorators import json_view


class ShowitemsViev(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'administration/control_items.html')


class ShowOrdersViev(LoginRequiredMixin, View):
    def get(self, request):

        orders = Orders.objects.all()

        return render(request, 'administration/control_orders.html', {"orders": orders})


@json_view
@login_required(login_url="/login/")
def order_info_view(request, id):
    try:
        order = Orders.objects.get(id=id)

    except:
        return {"success": False}

    title = _("Order info")
    order_items = OrderItems.objects.filter(order=order)

    t = loader.get_template("administration/order_info.html")
    c = {"order": order, "order_items": order_items}
    html = t.render(c, request)

    return {"success": True, "title": title, "html": html}


@json_view
@login_required(login_url="/login/")
def order_packed_view(request, id):
    try:
        order = Orders.objects.get(id=id)
        order.packed = True
        order.save()

    except:
        return {"success": False}

    return {"success": True}


@json_view
@login_required(login_url="/login/")
def order_delivery_view(request, id):
    try:
        order = Orders.objects.get(id=id)

    except:
        return {"success": False}
    title = _("Delivery info")

    t = loader.get_template("administration/order_delivery.html")
    c = {"order": order}
    html = t.render(c, request)

    return {"success": True, "title": title, "html": html}


@json_view
@csrf_exempt
@login_required(login_url="/login/")
def order_delivery_save_view(request, id):
    try:
        order = Orders.objects.get(id=id)

    except:
        return {"success": False}
    try:
        number = request.POST['number']
        if len(number) >= 1:
            order.ttn = number
            order.save()

            return {"success": True}
    except:
        return {"success": False}


@json_view
@login_required(login_url="/login/")
def order_payed_view(request, id):
    try:
        order = Orders.objects.get(id=id)

    except:
        return {"success": False}
    title = _("Payment info")

    t = loader.get_template("administration/order_payment.html")
    c = {"order": order}
    html = t.render(c, request)

    return {"success": True, "title": title, "html": html}


@json_view
@csrf_exempt
@login_required(login_url="/login/")
def order_payed_save_view(request, id):
    try:
        order = Orders.objects.get(id=id)
    except:
        return {"success": False}

    try:
        payed_sum = request.POST['sum']
        float(payed_sum)
    except:
        return {"success": False}

    payment = Payment()
    payment.order = order
    payment.amount = payed_sum
    payment.save()

    if order.get_total_price_grn() <= order.get_total_paid():
        order.paid = True
        order.save()

    return {"success": True}


@json_view
@csrf_exempt
@login_required(login_url="/login/")
def order_delete_view(request, id):
    try:
        order = Orders.objects.get(id=id)
        order.delete()
    except:
        return {"success": False}

    return {"success": True}