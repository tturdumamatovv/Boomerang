from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, Cart, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Cart
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')  # Используем атрибут 'name' для отображения названия продукта

    class Meta:
        model = OrderItem
        fields = ['product_name']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    total_price = serializers.ReadOnlyField()
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['products', 'delivery_address', 'payment_method', 'user', 'total_price']

    def get_products(self, obj):
        order_items = OrderItem.objects.filter(order=obj).select_related('product')
        serialized_products = OrderItemSerializer(order_items, many=True).data
        return serialized_products

    def create(self, validated_data):
        user = self.context['request'].user
        cart_items = Cart.objects.filter(user=user).select_related('product')
        if not cart_items.exists():
            raise ValidationError("Cart is empty")

        total_price = sum(item.product.price * item.quantity for item in cart_items)
        order = Order.objects.create(user=user, total_price=total_price, **validated_data)
        
        for cart_item in cart_items:
            OrderItem.objects.create(order=order, product=cart_item.product)

        cart_items.delete()
        return order

