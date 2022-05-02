from django.urls import path
from . import views

app_name = 'administration'
urlpatterns = [
    path('', views.Showitems.as_view(), name='showitems'),
    path('', views.Showorders.as_view(), name='showorders'),
]