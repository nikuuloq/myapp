from django.db import models
from django.contrib.auth.models import User

from ..beauty.models import Product

from django.conf import settings

class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='carts'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} {self.pk}'

    def total_price(self):
        return sum(item.total_price for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} {self.product.name}'

    def total_price(self):
        return self.quantity * self.product.price
