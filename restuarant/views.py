from django.shortcuts import render, redirect
from restuarant.models import Menu

# New import for Cart
from django.views import View


# Class based views
class Index(View):

    def post(self, request):
        item = request.POST.get('item')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(item)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(item)
                    else:
                        cart[item] = quantity - 1
                else:
                    cart[item] = quantity + 1
            else:
                cart[item] = 1
        else:
            cart = {}
            cart[item] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('resturant:pattern')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        appetisers = Menu.objects.filter(title='Appetisers')
        salads = Menu.objects.filter(title='Salads')
        starters = Menu.objects.filter(title='Starters')
        main_dishes = Menu.objects.filter(title='Main_Dishes')
        return render(request, 'restuarant/index.html',
                      {'Appetisers': appetisers,
                       'Salads': salads,
                       'Starters': starters,
                       'Main_Dishes': main_dishes})


# def individual_food(request):
#     # menu_foods = Menu.objects.all()
#     appetisers = Menu.objects.filter(title='Appetisers')
#     salads = Menu.objects.filter(title='Salads')
#     starters = Menu.objects.filter(title='Starters')
#     main_dishes = Menu.objects.filter(title='Main_Dishes')
#     return render(request, 'restuarant/index.html',
#                   {'Appetisers': appetisers,
#                    'Salads': salads,
#                    'Starters': starters,
#                    'Main_Dishes': main_dishes})


# Create your views here.


def product_list(request):
    return render(request, 'restuarant/sections/product_list.html')


def add_to_cart(request):
    return render(request, 'restuarant/sections/cart.html')
