from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = []

urlpatterns += (
    i18n_patterns(
    path('', include('showcase.urls')),
    path('administration/', include('administration.urls')),
    path('orders/', include('orders.urls')),
    path('info/', include('info.urls')),
    path('admin/', admin.site.urls),
    )
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

