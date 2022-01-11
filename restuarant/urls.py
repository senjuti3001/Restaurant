from django.urls import path

from . import views

from restuarant.cart import Cart

app_name = 'resturant'

urlpatterns = [
    path('', views.Index.as_view(), name='pattern'),
    # path('', views.individual_food, name='pattern'),
    path('products/', views.product_list, name='product_list'),
    path('addcart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', Cart.as_view(), name='cart'),
]

