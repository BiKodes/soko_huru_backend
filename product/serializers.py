from dataclasses import fields
from itertools import product
from pyexpat import model
from tkinter import BROWSE
from unicodedata import category
from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField(read_only=True)

    def get_products(self, obj):
        all_products = Product.objects.filter(category=obj.id)
        return ProductSerializer(all_products, many=True).data

    class Meta:
        model = Category
        
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products"
        )