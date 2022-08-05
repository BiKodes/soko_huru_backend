from unicodedata import name
from django.urls import path
from product import views
from .api import api_add_to_cart, api_remove_from_cart, api_checkout

app_name = 'products'

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('search/', views.search),
    path('<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api_remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    path('api_checkout/', api_checkout, name='api_checkout')
]