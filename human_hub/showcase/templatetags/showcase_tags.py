from django import template
from django.utils.translation import gettext_lazy as _

from showcase.models import Items, Photo, Categories, Sizes, Balance

register = template.Library()


@register.simple_tag
def get_categories():
    print("GET CATTTTTTTTTTTTTTTEGORIES")
    try:
        categories = Categories.objects.all()
    except:
        return ''

    return categories
