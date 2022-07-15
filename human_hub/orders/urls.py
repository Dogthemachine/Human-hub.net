from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [

    path('cart/', views.cart, name='cart'),
    path("cart/<int:id>/remove/", views.cart_remove, name="cart_remove"),
    path("cart/<int:id>/<int:size_id>/add/", views.cart_add, name="cart_add"),
    path("cart/checkout/", views.cart_checkout, name="cart_checkout"),
    path('order/', views.order, name='make_order'),
    path('order/submit/', views.submit, name='make_order'),
    path('order/payment/', views.submit, name='make_order'),
    path("wfp_callback/", views.wfp_callback, name="wfp_callback"),
]


