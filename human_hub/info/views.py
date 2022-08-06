from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from info.models import AboutPage, ContactsPage, DiscountsPage, SizingPage, ShippingPage, RefundPage, TermsPage, InfoPages


class AboutView(View):
    def get(self, request):
        try:
            content = AboutPage.objects.all()[0]
            return render(request, 'info/about.html', {'content': content})
        except:
            return render(request, 'info/about.html')


class AboutTagView(View):
    def get(self, request, tag=''):
        try:
            content = InfoPages.objects.filter(tag=tag)[0]
            return render(request, 'info/about.html', {'content': content})
        except:
            return render(request, 'info/about.html')


class ContactsView(View):
    def get(self, request):
        try:
            content = ContactsPage.objects.all()[0]
            return render(request, 'info/contacts.html', {'content': content})
        except:
            return render(request, 'info/contacts.html')


class DiscountsView(View):
    def get(self, request):
        try:
            content = DiscountsPage.objects.all()[0]
            return render(request, 'info/discounts.html', {'content': content})
        except:
            return render(request, 'info/discounts.html')


class RefundView(View):
    def get(self, request):
        try:
            content = RefundPage.objects.all()[0]
            return render(request, 'info/refund.html', {'content': content})
        except:
            return render(request, 'info/refund.html')


class ShippingView(View):
    def get(self, request):
        try:
            content = ShippingPage.objects.all()[0]
            return render(request, 'info/shipping.html', {'content': content})

        except:
            return render(request, 'info/shipping.html')


class SizingView(View):
    def get(self, request):
        try:
            content = SizingPage.objects.all()[0]
            return render(request, 'info/sizing.html', {'content': content})
        except:
            return render(request, 'info/sizing.html')


class TermsView(View):
    def get(self, request):
        try:
            content = TermsPage.objects.all()[0]
            return render(request, 'info/terms.html', {'content': content})
        except:
            return render(request, 'info/terms.html')