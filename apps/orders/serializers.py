from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from apps.beauty.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.name")
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ("id", "product", "product_name", "quantity", "price", "total_price")

    def get_total_price(self, obj):
        return obj.quantity * obj.price


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ("id", "user", "status", "address", "created_at", "items", "total_price")
        read_only_fields = ("user", "status", "created_at", "total_price")

    def get_total_price(self, obj):
        return sum([item.total_price() for item in obj.items.all()])

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item in items_data:
            product = item["product"]
            quantity = item["quantity"]
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price  # sipariş anındaki fiyat
            )
        return order
