from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


class AboutView(View):
    def get(self, request):
        return render(request, 'info/about.html')


class ContactsView(View):
    def get(self, request):
        return render(request, 'info/contacts.html')


class DiscountsView(View):
    def get(self, request):
        return render(request, 'info/discounts.html')


class RefundView(View):
    def get(self, request):
        return render(request, 'info/refund.html')


class ShippingView(View):
    def get(self, request):
        return render(request, 'info/shipping.html')


class SizingView(View):
    def get(self, request):
        return render(request, 'info/sizing.html')


class TermsView(View):
    def get(self, request):
        return render(request, 'info/terms.html')
