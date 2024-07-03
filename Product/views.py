from django.shortcuts import render
from Product.models import ProductModel
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem

# Create your views here.

def product_list(request):
    products = ProductModel.objects.all()
    return render(request, 'product/product_list.html', {'products': products})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('product:view_cart')


@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in cart_items)
    estimated_tax = total_price * 1
    shipping_cost = 5
    total = total_price + estimated_tax + shipping_cost

    context = {
        'cart_items':cart_items,
        'total_price':total_price,
        'estimated_tax':estimated_tax,
        'shipping_cost':shipping_cost,
        'total':total,
    }
    return render(request, 'product/cart.html', context=context)
    

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('product:view_cart')

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in cart_items)
    estimated_tax = total_price * 1  # Example tax calculation, adjust as needed
    total = total_price + estimated_tax

    context = {
        'cart_items':cart_items,
        'total_price':total_price,
        'estimated_tax':estimated_tax,
        'total':total,
    }
    return render(request, 'product/checkout.html', context=context)
