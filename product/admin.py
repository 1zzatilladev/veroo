from django.contrib import admin
from .models import Cart,Category,Product,Order

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id',  'name', 'created_at']
    search_fields = ['name']
    list_filter = ['name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'payment_type', 'address','total_price']
    search_fields = ['address']
    list_filter = ['user']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price','stock','created_at']
    search_fields = ['name','price','image']
    list_filter = ['name']


admin.site.register(Cart)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)