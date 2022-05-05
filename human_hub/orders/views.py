from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


class ShowCartView(View):
    def get(self, request):
        return render(request, 'orders/cart.html')


class MakeOrderView(View):
    def get(self, request):
        return render(request, 'orders/make_order.html')