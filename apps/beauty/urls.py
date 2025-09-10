from django.urls import path
from .views import (
    home,
    CategoryListCreateAPI, CategoryDetailAPI,
    ProductCreateAPI, ProductDetailAPI, ProductUpdateAPI, ProductDeleteAPI
)

urlpatterns = [
    # HTML
    path("", home, name="home"),
    path("categories/", CategoryListCreateAPI.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetailAPI.as_view(), name="category-detail"),
    path("products/", ProductCreateAPI.as_view(), name="product-list-create"),
    path("products/<int:pk>/", ProductDetailAPI.as_view(), name="product-detail"),
]
