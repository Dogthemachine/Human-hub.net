from django.urls import path
from . import views

app_name = 'showcase'

urlpatterns = [
    path('', views.ShowcaseView.as_view(), name='showcase'),
    path('category/<int:category_id>/', views.CategoryPageView.as_view(), name='category_page'),
    path('item/<int:item_id>/', views.ItemPageView.as_view(), name='item_page'),
    path('category/<int:item_id>/sizes/', views.ChooseSizes, name='choose_sizes'),
    path("currency/<str:valuta>/", views.cart_val, name="currency"),
]