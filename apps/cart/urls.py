from django.urls import path
from .views import CartListView, CartAddView, CartRemoveView, CartUpdateView, CartCheckoutView

urlpatterns = [
    path('', CartListView.as_view(), name='cart-list'),
    path('add/', CartAddView.as_view(), name='cart-add'),
    path('remove/<int:pk>/', CartRemoveView.as_view(), name='cart-remove'),
    path('update/<int:pk>/', CartUpdateView.as_view(), name='cart-update'),
    path('checkout/', CartCheckoutView.as_view(), name='cart-checkout'),

]
