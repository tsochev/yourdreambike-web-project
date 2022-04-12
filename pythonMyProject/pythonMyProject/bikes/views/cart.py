import json
from django.http import JsonResponse
from django.shortcuts import render

from django.views import generic as views

from pythonMyProject.bikes.models import Order, SellBike, OrderItem


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.id
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

        context = {
            'items': items,
            'order': order,
            'cart_items': cart_items,
        }

        return render(request, 'store/cart.html', context)


def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.id
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

        context = {
            'items': items,
            'order': order,
            'cart_items': cart_items,
        }

        return render(request, 'store/checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    bikeId = data['bike']
    action = data['action']

    print('Action:', action)
    print('bikeId:', bikeId)

    customer = request.user.id
    bike = SellBike.objects.get(id=bikeId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=bike)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)
