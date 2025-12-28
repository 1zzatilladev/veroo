from django.urls import path
from .views import home_page, add_to_cart, cart_view

urlpatterns = [
    path('', home_page, name='home'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
]
