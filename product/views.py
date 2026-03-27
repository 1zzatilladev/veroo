from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Cart, Order


def home_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    query = request.GET.get('q', '').strip()

    if query:
        products = products.filter(name__icontains=query) | products.filter(brend__icontains=query)

    return render(request, 'index.html', {
        'products': products,
        'categories': categories,
        'query': query,
    })


def category_view(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    return render(request, 'index.html', {
        'products': products,
        'categories': categories,
        'active_category': category,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item = Cart.objects.filter(
        user=request.user,
        product=product,
        order__isnull=True,
    ).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect('cart')


@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('cart')


@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user, order__isnull=True)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


@login_required
def checkout_view(request):
    cart_items = Cart.objects.filter(user=request.user, order__isnull=True)
    total = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        if not cart_items:
            return redirect('cart')

        payment_type = request.POST.get('payment_type', 'cash')
        address = request.POST.get('address', '')

        order = Order.objects.create(
            user=request.user,
            total_price=total,
            payment_type=payment_type,
            address=address,
        )
        cart_items.update(order=order)
        return redirect('orders')

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total})


@login_required
def orders_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')
    return render(request, 'orders.html', {'orders': orders})
