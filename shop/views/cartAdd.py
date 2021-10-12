from django.shortcuts import render
from ..models.product import Product 


products = []
def cartAdd(request, pk):
    cart_session = request.session.get('cart_session')
    product_cart = Product.objects.filter(id=cart_session)
    print(cart_session)
    product_pk = Product.objects.get(pk=pk)
    products.append(product_pk)

    return render(request, 'cart.html', {'products': products, 'products_sum':"чекни корзину", 'product_cart':product_cart})