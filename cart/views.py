from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart as CartModel
from movie.models import Movie as MovieModel
from django.contrib import messages

# Create your views here.


class Cart(LoginRequiredMixin, View):
    http_method_names = ['get', 'post', 'put', 'delete']
    login_url = '/user/login/'
    redirect_field_name = '/'


    def post(self, request, id):
        # try:
        #     cart = request.session["cart"]
        #     cart.append(id)
        #     print('d')
        #     request.session["cart"] = cart
        # except:
        #     cart = []
        #     cart.append(id)
        #     print('f')
        #     request.session["cart"] = cart
        # return HttpResponse(cart)

        # print(request.user.username)
        try:
            movie = MovieModel.objects.get(id=id)
            # CartModel.objects.create(user=request.user, quantity=1, movies=movie)
            cart = CartModel.objects.get(movies=movie, user=request.user)
            # messages.add_message(request, messages.SUCCESS, 'Added')
            messages.success(request, "Added")
        except:
            CartModel.objects.create(user=request.user, quantity=1, movies=movie)
            messages.add_message(request, messages.SUCCESS, 'Added')
        finally:
            return HttpResponseRedirect('/')

    def put(self, request, id):
        return HttpResponse("PUT")


    def delete(self, request, id):
        return HttpResponse("DELETE")


class MyCart(LoginRequiredMixin, View):
    login_url = '/user/login/'
    redirect_field_name = '/'

    def get(self, request):
        carts = CartModel.objects.filter(user=request.user).order_by('movies')
        return render(request, 'cart/index.html', {'carts' : carts})



@login_required()
def put_view(request, id):
    try:
        # CartModel.objects.create(user=request.user, quantity=1, movies=movie)

        if request.POST['quantity'] is not None:
            cart = CartModel.objects.get(id=id)
            if int(request.POST['quantity']) > cart.movies.in_stock or int(request.POST['quantity']) <= 0:
                raise ValueError
            cart.quantity = request.POST['quantity']
            cart.save()
            messages.success(request, "Updated")
        return HttpResponseRedirect('/cart/index/')
    except Exception as e:
        messages.success(request, "Too much")
        return HttpResponseRedirect('/cart/index/')
    finally:
        return HttpResponseRedirect('/cart/index/')
    return HttpResponse("put")



@login_required()
def delete_view(request, id):
    try:
        CartModel.objects.filter(id=id).delete()
        messages.success(request, "Removed")

    except:
        return HttpResponseRedirect('/cart/index/')
    finally:
        return HttpResponseRedirect('/cart/index/')
