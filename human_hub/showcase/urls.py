from django.urls import path
from . import views

app_name = 'showcase'

urlpatterns = [
    path('', views.ShowcaseView.as_view(), name='showcase'),
    path('category/', views.CategoryPageView.as_view(), name='category_page'),
    path('item/', views.ItemPageView.as_view(), name='item_page'),
]