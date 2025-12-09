from django.contrib import admin
from .models import Cart,Category,Product,Order
# Register your models here.
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)