from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.cart import Cart
from store.models import Product
from accounts.models import Profile
from .forms import CheckoutForm
from .models import Order, OrderItem


@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, 'سلة التسوق فارغة.')
        return redirect('store:product_list')

    profile_obj, _ = Profile.objects.get_or_create(user=request.user)
    initial_data = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'phone': profile_obj.phone,
        'address': profile_obj.address,
        'city': profile_obj.city,
    }

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.get_total_price()
            order.save()

            for item in cart:
                product = item['product']
                if item['quantity'] > product.stock:
                    messages.error(
                        request,
                        f'الكمية المطلوبة لـ {product.name} غير متوفرة. المتوفر: {product.stock}',
                    )
                    order.delete()
                    return redirect('cart:cart_detail')

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=item['price'],
                    quantity=item['quantity'],
                )
                product.stock -= item['quantity']
                product.save()

            cart.clear()
            messages.success(request, f'تم إنشاء طلبك بنجاح! رقم الطلب: #{order.id}')
            return redirect('orders:order_detail', order_id=order.id)
    else:
        form = CheckoutForm(initial=initial_data)

    return render(request, 'orders/checkout.html', {
        'form': form,
        'cart': cart,
    })


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
