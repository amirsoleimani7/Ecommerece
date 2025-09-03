from django.shortcuts import render , redirect
from .models import Product , CartItem


def product_list(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request , 'catalog/main_menu.html' , context)

def product_detail(request , pk):
    product = Product.objects.get(pk=pk)
    context = {
        "product" : product
    }
    return render(request,'catalog/detail.html',context)


def cart_view(reqeust):
    
    cart_items = CartItem.objects.filter(user=reqeust.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(reqeust , 'catalog/cart.html' , {'cart_items' : cart_items , 'total_price' : total_price})


def add_to_cart(request , product_id):
    product = Product.objects.get(id=product_id)
    cart_item , created = CartItem.objects.get_or_create(product=product ,user=request.user)
    cart_item.quantity += 1 
    cart_item.save()
    return redirect("cart_view")

def remove_from_cart(request , item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart_view')

