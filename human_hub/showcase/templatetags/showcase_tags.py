from django import template
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404

from showcase.models import Items, Photo, Categories, Sizes, Balance, Config

register = template.Library()


@register.simple_tag
def get_categories(request):

    html_categories = ""
    categories = Categories.objects.all()
    lang = request.LANGUAGE_CODE
    for cat in categories:
        html_categories += '<ul class ="nav navbar-nav navbar-right ms-2 mt-4 mb-0 h1 fs-5" ><li class="nav-item ' \
                           'visible-xs"><a class="nav-link hb-main-menu-color" style="font-family: IBM Plex Mono;" ' \
                           'href="/' + lang + '/' + 'category/' + str(cat.id) + '/" title="{% trans' + "'Category'" + '%}">'
        html_categories += cat.name
        html_categories += '</a></li></ul>'

    return mark_safe(html_categories)


def price_description(request):
    config = Config.objects.get()
    description = ''
    if request.session['valuta']=='grn':
        description = config.price_description
    if request.session['valuta']=='usd':
        description = config.price_description_usd
    if request.session['valuta']=='eur':
        description = config.price_description_eur

    return description


def get_price_description(request):
    html = price_description(request)
    return mark_safe(html)


@register.simple_tag
def get_price_itempage(request, item_id):
    this_item = get_object_or_404(Items, id=item_id)
    price = this_item.price
    if request.session['valuta'] != 'grn':
        config = Config.objects.get()
        rate = 1
        if request.session['valuta'] == 'usd':
            rate = config.dollar_rate
        if request.session['valuta'] == 'eur':
            rate = config.euro_rate
        price = round(price / rate, 2)
    price = str(price)

    html = price + ' ' + price_description(request)

    return mark_safe(html)