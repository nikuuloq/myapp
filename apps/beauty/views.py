from django.shortcuts import render
from .models import Category, Product
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response

# === FRONTEND VIEWS ===

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'home.html', context)

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products_list.html', {'products': products, 'categories': categories})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def delivery_info(request):
    return render(request, 'delivery_info.html')

# === API VIEWS (DRF) ===

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContactInfoViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "Contact info API not implemented"})

class DeliveryInfoViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "Delivery info API not implemented"})

class CartItemViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "Cart API not implemented"})
