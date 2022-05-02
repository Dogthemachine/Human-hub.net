from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.CatList.as_view(), name='all'),
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('breeds/', views.BreedList.as_view(), name='breed_all'),
    path('breed/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('breed/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
    path('breed/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
]