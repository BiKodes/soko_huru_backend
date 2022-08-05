from datetime import datetime
from django.http import Http404
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category, Product, ProductReview
from .serializers import ProductSerializer, CategorySerializer

class LatestProductsList(APIView):
   
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        product.num_visits = product.num_visits + 1
        product.last_visit = datetime.now()
        product.save()

        serializer = ProductSerializer(product)
        return Response(serializer.data)

def product_images(request, slug):
    product = get_object_or_404(Product, slug=slug)

    imagesstring = "{'thumbnail': '%s', 'image': '%s'}," % (
        product.get_thumbnail, product.image.url)
    
    for image in product.images.all():
        imagesstring = imagesstring + ("{'thumbnail': '%s', 'image': '%s'}," % (
            image.thumbnail.url, image.image.url
        ))

    context = {
        'product': product,
        'imagesstring': imagesstring
    }

    return render(request, context)

def product_review(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')

        review = ProductReview.objects.create(
            product=product,
            user=request.user,
            stars=stars,
            content=content)
        return redirect('product_detail', category_slug=category_slug, slug=slug)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})


        