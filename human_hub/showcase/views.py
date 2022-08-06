from jsonview.decorators import json_view
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.translation import gettext_lazy as _
from showcase.models import Photo, Categories, Items, Sizes, Balance, Banner


class ShowcaseView(View):
    def get(self, request):
        banner = Banner.objects.all()[0]
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
                'banner': banner,
            },
        )


class CategoryPageView(View):
    def get(self, request, category_id):
        banner = Banner.objects.all()[0]
        cat = get_object_or_404(Categories, id=category_id)
        items = Items.objects.filter(category=category_id)

        return render(
            request,
            'showcase/category_page.html',
            {
                'category': cat,
                'items': items,
                'banner': banner,
            }
        )


class ItemPageView(View):
    def get(self, request, item_id):
        item = get_object_or_404(Items, id=item_id)
        photos = Photo.objects.all().filter(item=item)
        sizes = Sizes.objects.all().filter(categories=item.category)
        for size in sizes:
            size.amount = Balance.objects.get(item=item, size=size).amount

        return render(
            request,
            'showcase/item_page.html',
            {
                'item': item,
                'photos': photos,
                'sizes': sizes,
            }
        )


@csrf_exempt
@json_view
def ChooseSizes(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    sizes = Sizes.objects.all().filter(categories=item.category)

    for size in sizes:
        size.amount = Balance.objects.get(item=item, size=size).amount

    t = loader.get_template('showcase/choose_sizes.html')
    c = {'sizes': sizes, 'item': item}
    html = t.render(c, request)

    return {'success': True, 'html': html}


@json_view
def cart_val(request, valuta):
    request.session['valuta'] = valuta

    return {'success': True}
