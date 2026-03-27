from django.urls import path
from .views import (
    home_page,
    category_view,
    product_detail,
    add_to_cart,
    remove_from_cart,
    cart_view,
    checkout_view,
    orders_view,
)

urlpatterns = [
    path('', home_page, name='home'),
    path('category/<int:category_id>/', category_view, name='category'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('orders/', orders_view, name='orders'),
]
