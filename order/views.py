from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ShipmentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from cart.models import Cart

from .models import Order, MovieStatus, MovieOrder

# Create your views here.



class Checkout(LoginRequiredMixin, View):
    login_url = '/user/login/'
    redirect_field_name = '/order/checkout/'


    def get(self, request):
        form = ShipmentForm()
        carts = Cart.objects.filter(user=request.user)
        return render(request, 'order_checkout/checkout.html', {'form' : form, 'carts' : carts})

    def post(self, request):
        form = ShipmentForm(request.POST or None)
        if form.is_valid():
            shipment = form.save()
            try:
                carts = Cart.objects.filter(user=request.user)
                MovieStatus.objects.get_or_create(name='Process')
                status = MovieStatus.objects.get(name='Process')
                order = Order(customer=request.user, status=status, shipment=shipment)
                order.save()
                for cart in carts:
                    movie_order = MovieOrder(movies=cart.movies, order=order, number_of_movie=cart.quantity)
                    movie_order.save()
                clear_cart(request.user)
                return render(request,'order_checkout/success.html', {'message': 'Checkout success'})
            except Exception as e:
                return render(request,'order_checkout/success.html', {'message': 'Checkout fail'})
            # form.save()
        return HttpResponse("con accac")

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except:
        return False

def validate_int(int_text):
    try:
        inter = int(int_text) + 1
        return True
    except:
        return False
class OrderList(LoginRequiredMixin, ListView):
    login_url = '/user/login/'
    redirect_field_name = '/order'
    queryset = MovieOrder.objects.all()
    # limit 10 movies per page /?page=1
    template_name = 'order_checkout/index.html'


    # def get(self, request):
    #     movies = MovieOrder.objects.filter(order__customer=request.user)
    #     return render(request, 'order_checkout/index.html',{'movies' : movies})

    def get_queryset(self):
        qs = MovieOrder.objects.filter(order__customer=self.request.user).order_by('order__date_make_order');
        query = self.request.GET.get('order')
        if query is not None:

            if validate_int(query):
                print(query)
                qs = qs.filter(
                    Q(order__id=query)
                )
            elif validate_date(query):
                qs = qs.filter(
                    Q(order__date_make_order=query)
                )
            else:

                qs = qs.filter(
                    Q(movies__name__icontains=query)
                )
            # print(query)

        return qs


def clear_cart(user):
    Cart.objects.filter(user=user).delete()

@login_required()
def cancel_order(request, id):
    order = Order.objects.get(id=id)
    MovieStatus.objects.get_or_create(name='Cancel')
    status = MovieStatus.objects.get(name='Cancel')
    order.status = status
    order.save()
    messages.success(request, "Cancelled")
    return HttpResponseRedirect('/order/index/')