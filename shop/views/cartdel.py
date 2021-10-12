from django.shortcuts import render
from ..models.product import Product
from .cartAdd import products

def delete(request, pk):
        product_pk = Product.objects.get(pk=pk)
        if product_pk in products:
            products.remove(product_pk)
        return render(request, 'cart.html', {'products': products, 'products_sum':"чекни корзайн"})