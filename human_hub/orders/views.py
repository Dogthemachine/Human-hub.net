from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from jsonview.decorators import json_view
from django.template import loader, Context


class MakeOrderView(View):
    def get(self, request):
        return render(request, 'orders/make_order.html')


@json_view
def cart(request):
    # cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    # cart.session = request.session.session_key
    # cart.save()
    #
    # if not created:
    #     cart_items = CartItem.objects.filter(cart=cart)
    #     for c_i in cart_items:
    #         c_i.bal = Balance.objects.get(item=c_i.item, size=c_i.size).amount
    # else:
    #     cart_items = []

    t = loader.get_template('orders/cart.html')
    # c = {'cart': cart, 'cart_items': cart_items}

    html = t.render({}, request)

    return {'html': html}


@json_view
def order(request):
    t = loader.get_template('orders/make_order.html')
    html = t.render({}, request)

    return {'html': html}


