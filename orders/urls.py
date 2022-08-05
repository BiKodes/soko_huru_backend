from unicodedata import name
from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()), 
    path('order_confirmation/', views.order_confirmation, name='')
]