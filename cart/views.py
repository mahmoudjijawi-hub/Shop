from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from store.models import Product
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, available=True)
    quantity = int(request.POST.get('quantity', 1))

    if quantity > product.stock:
        messages.warning(request, f'الكمية المتاحة لـ {product.name} هي {product.stock} فقط.')
        quantity = product.stock

    if quantity > 0:
        cart.add(product=product, quantity=quantity)
        messages.success(request, f'تمت إضافة {product.name} إلى السلة.')

    next_url = request.POST.get('next', 'cart:cart_detail')
    if next_url.startswith('/'):
        return redirect(next_url)
    return redirect(next_url)


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'تمت إزالة {product.name} من السلة.')
    return redirect('cart:cart_detail')


@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, available=True)
    quantity = int(request.POST.get('quantity', 1))

    if quantity > product.stock:
        messages.warning(request, f'الكمية المتاحة لـ {product.name} هي {product.stock} فقط.')
        quantity = product.stock

    cart.update_quantity(product, quantity)
    return redirect('cart:cart_detail')
