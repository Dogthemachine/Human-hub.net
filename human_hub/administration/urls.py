from django.urls import path
from . import views

app_name = 'administration'

urlpatterns = [
    path('orders/', views.ShowOrdersViev.as_view(), name='showorders'),
    path("orders/<int:id>/info/", views.order_info_view, name="order_info"),
    path("orders/<int:id>/packed/", views.order_packed_view, name="order_packed"),
    path("orders/<int:id>/delivery/", views.order_delivery_view, name="order_delivery"),
    path("orders/<int:id>/delivery-save/", views.order_delivery_save_view, name="order_delivery_save"),
    path("orders/<int:id>/payed/", views.order_payed_view, name="order_payed"),
    path("orders/<int:id>/payed-save/", views.order_payed_save_view, name="order_payed_save"),
    path("orders/<int:id>/order-delete/", views.order_delete_view, name="order_delete"),

]