from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from .views import Checkout, OrderList, cancel_order
urlpatterns = [
    path('checkout/', Checkout.as_view(), name="checkout-index"),
    path('index/', OrderList.as_view(), name="order-index"),
    path('cancel/<int:id>', cancel_order, name="order-cancel")

]