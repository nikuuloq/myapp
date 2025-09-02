from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CartItem
from .serializers import CartItemSerializer
from apps.beauty.models import Product

from rest_framework.views import APIView
from apps.orders.models import Order, OrderItem
from apps.orders.serializers import OrderSerializer


# Sepeti görüntüle
class CartListView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


# Sepete ürün ekle
class CartAddView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity', 1))

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Ürün bulunamadı."}, status=status.HTTP_404_NOT_FOUND)

        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Sepetten ürün sil
class CartRemoveView(generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        try:
            cart_item = CartItem.objects.get(id=item_id, user=request.user)
            cart_item.delete()
            return Response({"message": "Ürün sepetten çıkarıldı."}, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({"error": "Ürün sepette bulunamadı."}, status=status.HTTP_404_NOT_FOUND)


# Sepetteki ürün adedini güncelle
class CartUpdateView(generics.UpdateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        quantity = int(request.data.get('quantity', 1))

        try:
            cart_item = CartItem.objects.get(id=item_id, user=request.user)
            cart_item.quantity = quantity
            cart_item.save()
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data)
        except CartItem.DoesNotExist:
            return Response({"error": "Ürün sepette bulunamadı."}, status=status.HTTP_404_NOT_FOUND)



class CartCheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Kullanıcının sepeti
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({"detail": "Sepet boş."}, status=400)

        # Sipariş oluştur
        order = Order.objects.create(user=request.user, address=request.data.get("address"))

        # CartItem'ları OrderItem'a çevir
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price  # sipariş anındaki fiyat
            )

        # Sepeti temizle
        cart_items.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=201)
