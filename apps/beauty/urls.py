from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'categories', views.CategoryViewSet, basename='categories')


urlpatterns = [
    path('', views.home, name='home'),  # главная страница
    path('products/', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),
    path('delivery/', views.delivery_info, name='delivery_info'),

    path('api/', include(router.urls)),  # API endpoints (DRF)
]
