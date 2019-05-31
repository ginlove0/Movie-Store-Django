from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import Cart, MyCart,put_view, delete_view
from . import views
urlpatterns = [
    path('index/', MyCart.as_view(), name="mycart"),
    path('<int:id>/', Cart.as_view(), name="cart-view"),
path('update/<int:id>/', put_view, name="putcart-view"),
    # url('', get_all_cart, name="cart-index"),
path('delete/<int:id>/', delete_view, name="deletecart-view"),
]