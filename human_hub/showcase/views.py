from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta
from django.utils import timezone
from showcase.models import Photo, Categories, Items, Sizes, Balance


class ShowcaseView(View):

    def get(self, request):

        cat = Categories.objects.all()
        categories = []

        for category in cat:
            categories.append((category.get_first2items(), category.get_rest_items(), category,))
        if cat:
            title_tag = cat[0].title_tag
            description_tag = cat[0].description_tag
        else:
            title_tag = _("main pae title_tag")
            description_tag = _("main pae description_tag")

        return render(
            request,
            'showcase/showcase.html',
            {
                "categories": categories,
                "title_tag": title_tag,
                "description_tag": description_tag,
            },
        )


class CategoryPageView(View):

    def get(self, request, category_id):
        cat = get_object_or_404(Categories, id=category_id)
        items = Items.objects.filter(category=category_id)
        return render(
            request,
            'showcase/category_page.html',
            {
                'category': cat,
                'items': items,
            }

        )


class ItemPageView(View):

    def get(self, request, item_id):
        item = get_object_or_404(Items, id=item_id)

        photos = Photo.objects.all().filter(item=item)

        sizes = Sizes.objects.all().filter(categories=item.category)

        print(photos.count())
        return render(
            request,
            'showcase/item_page.html',
            {
                'item': item,
                'photos': photos,
                'sizes': sizes,
            }
        )