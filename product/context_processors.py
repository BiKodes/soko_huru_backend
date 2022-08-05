from unicodedata import category
from .models import Category

def menu_categories(request):
    categories = Category.objects.filter(parent=None)
    
    return category