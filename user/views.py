from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

class UserSignup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('/user/login/')
    template_name = 'registration/signup.html'

class UserLogin(View):

    def get(self, request):
        return render(request)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})