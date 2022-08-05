from unicodedata import category, name
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from .sitemaps import CategorySitemap, ProductSitemap

sitemaps = {
    'product': ProductSitemap,
    'category': CategorySitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/products/', include('product.urls', namespace='products')),
    path('api/v1/orders/', include('orders.urls', namespace='orders')),
    path('api/v1/cart/', include('cart.urls', namespace='cart')),
    path('api/v1/coupon/', include('coupon.urls', namespace='coupon')),
    path('api/v1/userprofile/', include('coupon.urls', namespace='coupon')),

    path(
        'sitemap.xml', sitemap, {'sitemaps': sitemaps}, 
        name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
