from django.urls import path
from .views.homepage import homepage, HomePageView
from .views.detail import detail
from .views.cart import cart
from .views.register import register
from .views.signin import signin
from .views.signout import signout
from .views.cart import addToCard, remove_from_cart
from .views.categoory import pr_by_category
from .views.search import search
from .views.order import order


urlpatterns = [
    path('', homepage, name='homepage'),
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>', detail, name="detail"),
    path('cart', cart, name='cart'),
    path('register', register, name='register'),
    path('signin/' , signin, name='signin'),
    path('signout', signout, name='signout'),
    path('addToCart/<int:pk>', addToCard, name='addToCart'),
    path('remove_from_cart/<int:pk>', remove_from_cart, name='remove_from_cart'),
    path('category/<int:pk>', pr_by_category, name='pr_by_category'),
    path('search', search, name='search'),
    path('order', order, name='order'),
]