from django.shortcuts import render
from rest_framework import generics
from .models import Product
from rest_framework.views import APIView
from .models import Wishlist, Rating, Comment
from .serializers import WishlistSerializer, RatingSerializer, CommentSerializer
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


# HTML için home view
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, "beauty_home.html", {
        "categories": categories,
        "products": products,
    })


# API: Kategoriler
class CategoryListCreateAPI(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# API: Ürünler
class ProductCreateAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def contacts(request):
    return render(request, "contacts.html")


def product_list(request):
    products = Product.objects.all()

    # kategori filtresi
    category = request.GET.get("category")
    if category:
        products = products.filter(category__name=category)

    # fiyat filtresi
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)

    return render(request, "beauty_home.html", {"products": products})


# --------- Wishlist API ----------
class WishlistListCreateAPI(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


class WishlistDetailAPI(generics.RetrieveDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


# --------- Rating API ----------
class RatingListCreateAPI(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RatingDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


# --------- Comment API ----------
class CommentListCreateAPI(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
