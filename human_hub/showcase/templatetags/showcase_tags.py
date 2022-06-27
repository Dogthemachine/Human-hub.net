from django import template
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


from showcase.models import Items, Photo, Categories, Sizes, Balance

register = template.Library()


@register.simple_tag
def get_categories(request):

    html_categories = ""
    categories = Categories.objects.all()
    for cat in categories:
        html_categories += '<ul class ="nav navbar-nav navbar-right ms-2 mt-4 mb-0 h1 fs-5" ><li class="nav-item visible-xs"><a class="nav-link hb-main-menu-color" style="font-family: IBM Plex Mono;" href="/category/' + str(cat.id) + '/" title="{% trans' + "'Category'" + '%}">'
        html_categories += cat.name
        html_categories += '</a></li></ul>'
        print(html_categories)

    return mark_safe(html_categories)
