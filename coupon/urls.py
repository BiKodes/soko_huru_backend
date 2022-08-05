from unicodedata import name
from django.urls import path

from .api import api_can_use


app_name = 'cuopon '

urlpatterns = [
    path('/api/', api_can_use, name='api_can_use'),
    
]