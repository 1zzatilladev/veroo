from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    image = models.ImageField(upload_to="product/")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50,choices=[
        ("cash","Naxt pul"),
        ("cart" , "Carta orqali "),
        ("click","click orqali"),
    ])
    address=models.TextField(blank=True,null=True)
    total_price=models.DecimalField(max_digits=100, decimal_places=2)
    status=models.CharField(max_length=100, choices=[
        ("new" ,"yangi"),
        ("accepted" , "Qabul qilingan"),
        ("in_progress","Jarayonda"),
        ("delivering" , "Yetkazilmoqda.."),
        ("deliveried","Yetkazilgan"),
        ("cenceled","Bekor qilingan"),
    ])

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name



