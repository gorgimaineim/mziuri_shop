from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>', views.product_detail, name='product_detail'),
    path('create_product/', views.create_product, name='create_product'),
    path('update_product/<int:id>', views.update_product, name='update_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add_product_to_cart/<int:id>', views.add_product_to_cart, name='add_product_to_cart'),
    path('remove_cart_item/<int:id>', views.remove_cart_item, name='remove_cart_item'),
    path('confirm_purchase/', views.confirm_purchase, name='confirm_purchase'),
]
