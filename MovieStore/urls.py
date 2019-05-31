"""MovieStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import urls
from django.views.generic.base import TemplateView #displays home page



admin.site.site_header = "Movie Store"
admin.site.site_title = "Movie Store"
admin.site.index_title = "Movie Store"

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('staff/', admin.site.urls),
    # path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('cart/', include('cart.urls')),
    path('user/', include('user.urls')),
    path('user/', include(urls)),
    path('', include('movie.urls')),
    # path('', TemplateView.as_view(template_name='home.html'), name='home')  # display homepage

]


 #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

