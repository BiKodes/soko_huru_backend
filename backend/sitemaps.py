from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from product.models import Category, Product

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()

class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.date_added

