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
    path('about_tag/', views.AboutTagView.as_view(), {'tag': 'about'}, name='about_tag'),
    path('contacts_tag/', views.AboutTagView.as_view(), {'tag': 'contacts'}, name='contacts_tag'),
    path('about_tag/', views.AboutTagView.as_view(), {'tag': 'discounts'}, name='discounts_tag'),
    path('about_tag/', views.AboutTagView.as_view(), {'tag': 'refund'}, name='refund_tag'),
    path('about_tag/', views.AboutTagView.as_view(), {'tag': 'shipping'}, name='shipping_tag'),
    path('about_tag/', views.AboutTagView.as_view(), {'tag': 'sizing'}, name='sizing_tag'),
    path('about_tag/', views.AboutTagView.as_view(), {'tag': 'aboutermst'}, name='aboutermst_tag'),

]