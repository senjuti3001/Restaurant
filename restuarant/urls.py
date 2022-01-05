from django.urls import path

from . import views

app_name = 'resturant'

urlpatterns = [
    path('', views.individual_food, name='pattern'),
    path('products/', views.product_list, name='product_list'),
    path('cart/', views.add_to_cart, name='add_to_cart'),


   path('update_item/', views.updateItem, name='update_item'),
]

