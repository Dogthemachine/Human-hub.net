from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class ShowitemsViev(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'administration/control_items.html')


class ShowordersViev(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'administration/control_items.html')