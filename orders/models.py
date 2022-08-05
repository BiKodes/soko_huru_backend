from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

from product.models import Product
from . constants import *

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    paid_amount = models.CharField(max_length=100)
    used_coupon = models.CharField(max_length=255, blank=True)
    payment_intent = models.CharField(max_length=255, blank=True)

    shipped_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(choices= ORDER_STATUS_CHOICES , max_length=50, default="...")
    mpesa_token = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id