from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from info.models import AboutPage, ContactsPage, DiscountsPage, SizingPage, ShippingPage, RefundPage


class AboutView(View):

    def get(self, request):
        content = AboutPage.objects.all()[0]

        return render(request, 'info/about.html', {'content': content})


class ContactsView(View):

    def get(self, request):
        content = ContactsPage.objects.all()[0]
        return render(request, 'info/contacts.html', {'content': content})


class DiscountsView(View):

    def get(self, request):
        content = DiscountsPage.objects.all()[0]
        return render(request, 'info/discounts.html', {'content': content})


class RefundView(View):

    def get(self, request):
        content = RefundPage.objects.all()[0]
        return render(request, 'info/refund.html', {'content': content})


class ShippingView(View):

    def get(self, request):
        content = ShippingPage.objects.all()[0]
        return render(request, 'info/shipping.html', {'content': content})


class SizingView(View):

    def get(self, request):
        content = SizingPage.objects.all()[0]
        return render(request, 'info/sizing.html', {'content': content})


class TermsView(View):

    def get(self, request):
        return render(request, 'info/terms.html')
