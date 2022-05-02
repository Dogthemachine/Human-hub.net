import os
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve
from django.views.generic import TemplateView

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    url(r'^site/(?P<path>.*)$', serve, {'document_root': SITE_ROOT, 'show_indexes': True}, name='site_path'),
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('admin/', admin.site.urls),
    path('administration/', include('administration.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('orders/', include('orders.urls')),
    path('showcase/', include('showcase.urls')),
]
