import datetime
from itertools import product
import os

from random import randint

from .models import Order, OrderItem
from cart.cart import Cart

def checkout(request, first_name, last_name, email, address, postalcode, county, mobile_number):
    order = Order(
            first_name=first_name, last_name=last_name, email=email, 
            address=address, postalcode =postalcode, county =county,
            mobile_number=mobile_number)

    if request.user.is_authenticated:
        order.user = request.user
    order.save()
    
    cart =  Cart(request)

    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
            quantity=item['quantity'])

    return order.id

      