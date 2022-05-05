from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


class ShowcaseView(View):
    def get(self, request):
        return render(request, 'showcase/showcase.html')


class CategoryPageView(View):
    def get(self, request):
        return render(request, 'showcase/category_page.html')


class ItemPageView(View):
    def get(self, request):
        return render(request, 'showcase/item_page.html')