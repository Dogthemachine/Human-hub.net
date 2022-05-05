from django.urls import path
from . import views

app_name = 'administration'

urlpatterns = [
    path('balance/', views.ShowitemsViev.as_view(), name='showitems'),
    path('orders/', views.ShowordersViev.as_view(), name='showorders'),
]