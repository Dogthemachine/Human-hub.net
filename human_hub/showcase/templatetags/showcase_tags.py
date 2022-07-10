from django import template
from django.utils.safestring import mark_safe

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


@register.simple_tag
def get_price(entry, request):
    price = entry.price
    discount_price = entry.get_actual_price()
    if request.session['valuta'] == 'grn':
        if price == discount_price:
            html = '%s' % entry.get_actual_price()
        else:
            name = entry.get_discount_name()
            html = '<span class="icon-info cc-tooltip" data-toggle="tooltip" data-original-title="%s"></span>' % name
            html += ' <del>%s</del> %s' % (price, discount_price)
    else:
        config = Config.objects.get()
        rate = 1
        if request.session['valuta'] == 'usd':
            rate = config.dollar_rate
        if request.session['valuta'] == 'eur':
            rate = config.euro_rate
        price = round(price / rate, 2)
        discount_price = round(discount_price / rate, 2)
        if price == discount_price:
            html = '%s' % price
        else:
            name = entry.get_discount_name()
            html = '<span class="icon-info cc-tooltip" data-toggle="tooltip" data-original-title="%s"></span>' % name
            html += ' <del>%s</del> %s' % (price, discount_price)

    return mark_safe(html)


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