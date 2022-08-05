import json
from django.shortcuts import render
from django.template import context

from coupon.models import Coupon

from .cart import Cart

def cart_detail(request):

    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
           
        b = "{'id': '%s','thumbnail': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s'}," % (
                product.id, product.get_thumbnail, product.title, product.price, item['quantity']
            )

        productsstring = productsstring + b

    context = {
        'cart': cart,
        'productsstring': productsstring
    }
  
    return render(request, context)


