from django.urls import path
from .views import (
    home,
    CategoryListCreateAPI, CategoryDetailAPI,
    ProductListCreateAPI, ProductDetailAPI,
)

urlpatterns = [
    # HTML
    path("", home, name="home"),

    # API - Kategoriler
    path("api/categories/", CategoryListCreateAPI.as_view(), name="category-list-create"),
    path("api/categories/<int:pk>/", CategoryDetailAPI.as_view(), name="category-detail"),

    # API - Ürünler
    path("api/products/", ProductListCreateAPI.as_view(), name="product-list-create"),
    path("api/products/<int:pk>/", ProductDetailAPI.as_view(), name="product-detail"),
]
