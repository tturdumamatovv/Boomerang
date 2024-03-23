from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Product, Cart, Order
from .serializers import ProductSerializer, CartSerializer, OrderSerializer, OrderItemSerializer 

User = get_user_model()

class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@example.com', username='test_user', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.product_data = {'name': 'Test Product', 'description': 'Test Description', 'price': '10.00'}

    def test_create_product(self):
        response = self.client.post(reverse('product-list-create'), self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_product(self):
        product = Product.objects.create(name='Test Product', description='Test Description', price='10.00', owner=self.user)
        response = self.client.get(reverse('product-detail', args=[product.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CartAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@example.com', username='test_user', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(name='Test Product', description='Test Description', price='10.00', owner=self.user)
        self.cart_data = {'product': self.product.pk, 'quantity': 2}

    def test_create_cart_item(self):
        response = self.client.post(reverse('cart-create'), self.cart_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_cart_items(self):
        Cart.objects.create(user=self.user, product=self.product, quantity=2)
        response = self.client.get(reverse('cart-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@example.com', username='test_user', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(name='Test Product', description='Test Description', price='10.00', owner=self.user)
        self.order_data = {'delivery_address': 'Test Address', 'payment_method': 'Test Payment'}

    def test_create_order(self):
        cart_item = Cart.objects.create(user=self.user, product=self.product, quantity=2)
        response = self.client.post(reverse('order-create'), self.order_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProductSerializerTestCase(TestCase):
    def test_product_serializer(self):
        user = User.objects.create_user(email='test@example.com', username='test_user', password='testpassword')
        product_data = {'name': 'Test Product', 'description': 'Test Description', 'price': '10.00', 'owner': user}
        serializer = ProductSerializer(data=product_data)
        self.assertTrue(serializer.is_valid())


class CartSerializerTestCase(TestCase):
    def test_cart_serializer(self):
        user = User.objects.create_user(email='test@example.com', username='test_user', password='testpassword')
        product = Product.objects.create(name='Test Product', description='Test Description', price='10.00', owner=user)
        cart_data = {'user': user.pk, 'product': product.pk, 'quantity': 2}  # Обратите внимание на использование pk вместо объектов
        serializer = CartSerializer(data=cart_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)


class OrderSerializerTestCase(TestCase):
    def test_order_serializer(self):
        user = User.objects.create_user(email='test@example.com', username='test_user', password='testpassword')
        product = Product.objects.create(name='Test Product', description='Test Description', price='10.00', owner=user)
        order_data = {'user': user, 'delivery_address': 'Test Address', 'payment_method': 'Test Payment', 'total_price': '20.00'}
        serializer = OrderSerializer(data=order_data)
        self.assertTrue(serializer.is_valid())


class OrderItemSerializerTestCase(TestCase):
    def test_order_item_serializer(self):
        user = User.objects.create_user(email='test@example.com', username='test_user', password='testpassword')
        product = Product.objects.create(name='Test Product', description='Test Description', price='10.00', owner=user)
        order = Order.objects.create(user=user, delivery_address='Test Address', payment_method='Test Payment', total_price='20.00')
        order_item_data = {'order': order, 'product': product, 'quantity': 2}
        serializer = OrderItemSerializer(data=order_item_data)
        self.assertTrue(serializer.is_valid())
