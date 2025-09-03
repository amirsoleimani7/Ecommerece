from django.shortcuts import render
from .models import Product


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