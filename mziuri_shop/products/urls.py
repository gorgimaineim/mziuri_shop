from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>', views.product_detail, name='product_detail'),
    path('create_product/', views.create_product, name='create_product'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add_product_to_cart/<int:id>', views.add_product_to_cart, name='add_product_to_cart'),
]
