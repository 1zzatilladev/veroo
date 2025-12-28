#!/usr/bin/env python
import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from product.models import Category, Product

def create_sample_data():
    # Create categories
    categories = ['Elektronika', 'Kiyim-kechak', 'Uy-ro\'zg\'or', 'Sport', 'Kitoblar']
    for cat_name in categories:
        Category.objects.get_or_create(name=cat_name)

    # Sample products data
    products_data = [
        {'name': 'iPhone 15 Pro', 'brend': 'Apple', 'price': 15000000, 'stock': 10, 'category': 'Elektronika'},
        {'name': 'Samsung Galaxy S24', 'brend': 'Samsung', 'price': 12000000, 'stock': 15, 'category': 'Elektronika'},
        {'name': 'MacBook Air M3', 'brend': 'Apple', 'price': 25000000, 'stock': 5, 'category': 'Elektronika'},
        {'name': 'Nike Air Max', 'brend': 'Nike', 'price': 1200000, 'stock': 20, 'category': 'Kiyim-kechak'},
        {'name': 'Adidas Ultraboost', 'brend': 'Adidas', 'price': 1800000, 'stock': 12, 'category': 'Kiyim-kechak'},
        {'name': 'Levi\'s Jeans', 'brend': 'Levi\'s', 'price': 450000, 'stock': 25, 'category': 'Kiyim-kechak'},
        {'name': 'LG Smart TV 55"', 'brend': 'LG', 'price': 8500000, 'stock': 8, 'category': 'Elektronika'},
        {'name': 'Sony PlayStation 5', 'brend': 'Sony', 'price': 6500000, 'stock': 6, 'category': 'Elektronika'},
        {'name': 'Dyson Vacuum Cleaner', 'brend': 'Dyson', 'price': 3200000, 'stock': 10, 'category': 'Uy-ro\'zg\'or'},
        {'name': 'KitchenAid Mixer', 'brend': 'KitchenAid', 'price': 2800000, 'stock': 7, 'category': 'Uy-ro\'zg\'or'},
        {'name': 'Peloton Bike', 'brend': 'Peloton', 'price': 15000000, 'stock': 3, 'category': 'Sport'},
        {'name': 'Yoga Mat Premium', 'brend': 'Manduka', 'price': 350000, 'stock': 30, 'category': 'Sport'},
        {'name': 'Python Programming Book', 'brend': 'O\'Reilly', 'price': 120000, 'stock': 50, 'category': 'Kitoblar'},
        {'name': 'Machine Learning Guide', 'brend': 'Packt', 'price': 150000, 'stock': 40, 'category': 'Kitoblar'},
    ]

    created_count = 0
    for product_data in products_data:
        category = Category.objects.get(name=product_data['category'])
        product, created = Product.objects.get_or_create(
            name=product_data['name'],
            defaults={
                'brend': product_data['brend'],
                'price': product_data['price'],
                'stock': product_data['stock'],
                'category': category,
            }
        )
        if created:
            created_count += 1

    print(f'Created categories: {categories}')
    print(f'Added {created_count} new sample products')
    print(f'Total products in database: {Product.objects.count()}')

if __name__ == '__main__':
    create_sample_data()