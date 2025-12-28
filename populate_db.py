import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from product.models import Category, Product

# Create categories
categories = ['Elektronika', 'Kiyim-kechak', 'Uy-ro\'zg\'or', 'Sport', 'Kitoblar']
for cat_name in categories:
    Category.objects.get_or_create(name=cat_name)

# Get available images
media_dir = 'media/product'
available_images = []
if os.path.exists(media_dir):
    available_images = [f for f in os.listdir(media_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

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
for i, product_data in enumerate(products_data):
    category = Category.objects.get(name=product_data['category'])
    
    # Assign an image if available
    image_path = None
    if available_images and i < len(available_images):
        image_path = f'product/{available_images[i]}'
    
    product, created = Product.objects.get_or_create(
        name=product_data['name'],
        defaults={
            'brend': product_data['brend'],
            'price': product_data['price'],
            'stock': product_data['stock'],
            'category': category,
        }
    )
    
    # Update image if product was just created and we have an image
    if created and image_path:
        product.image = image_path
        product.save()
    
    if created:
        created_count += 1

print(f'Created categories: {categories}')
print(f'Available images: {len(available_images)}')
print(f'Added {created_count} new sample products')
print(f'Total products in database: {Product.objects.count()}')