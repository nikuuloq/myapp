from django.shortcuts import render
from .models import Category, Product

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'beauty/home.html', {
        'categories': categories,
        'products': products
    })
