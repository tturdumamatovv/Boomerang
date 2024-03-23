from django.urls import path
from product import views

urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('cart/', views.CartCreateAPIView.as_view(), name='cart-create'),
    path('cart/list/', views.CartListAPIView.as_view(), name='cart-list'),
    path('order/create/', views.OrderCreateAPIView.as_view(), name='order-create'),
    path('orders/', views.OrderListAPIView.as_view(), name='order-list'),

]
