from django.shortcuts import render
from django.http import JsonResponse
from .models import Menu
import json

# Create your views here.
def individual_food(request):
    # menu_foods = Menu.objects.all()
    appetisers = Menu.objects.filter(title='Appetisers')
    salads = Menu.objects.filter(title='Salads')
    starters = Menu.objects.filter(title='Starters')
    main_dishes = Menu.objects.filter(title='Main_Dishes')
    return render(request, 'restuarant/index.html',
                  {'Appetisers': appetisers,
                   'Salads': salads,
                   'Starters': starters,
                   'Main_Dishes': main_dishes})


def product_list(request):
    return render(request, 'restuarant/sections/product_list.html')


def add_to_cart(request):
    return render(request, 'restuarant/sections/cart.html')



def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

    return JsonResponse('Item was added', safe=False)