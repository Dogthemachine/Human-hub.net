from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('discounts/', views.DiscountsView.as_view(), name='discounts'),
    path('refund/', views.RefundView.as_view(), name='refund'),
    path('shipping/', views.ShippingView.as_view(), name='shipping'),
    path('sizing/', views.SizingView.as_view(), name='sizing'),
    path('terms/', views.TermsView.as_view(), name='terms'),
]