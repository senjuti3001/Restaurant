from django.shortcuts import render
from django.views import View
from .models import Menu


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        items = Menu.get_item_by_id(ids)
        print(items)
        return render(request, 'restuarant/sections/cart.html', {
            'items': items
        })
