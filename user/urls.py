from django.contrib import admin
from django.urls import path
from .views import UserSignup, register
from django.conf.urls import url
urlpatterns = [
    path('signup/', register, name="user-signup"),
]