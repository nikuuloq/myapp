from rest_framework import serializers

from .models import Cart, CartItem
from apps.beauty.models import Product


class DishSerializerForCart(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'price', 'image', 'name')


class CartItemSerializer(serializers.ModelSerializer):
    dish = DishSerializerForCart(read_only=True)
    dish_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='beauty_config',
        write_only=True
    )
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('id', 'quantity', 'dish', 'dish_id', 'total_price')

    def get_total_price(self, obj):
        # Убедиться, что `obj` это экземпляр модели
        if isinstance(obj, CartItem):
            return obj.total_price()

        raise ValueError("Объект должен быть экземпляром модели CartItem")


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('id', 'user', 'created_at', 'items', 'total_price')

    def get_total_price(self, obj):
        return obj.total_price()
