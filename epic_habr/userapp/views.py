from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

import sys

sys.path.append('../')

from userapp.forms import UserLoginForm, UserRegistrationForm


# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm()
    title = 'Авторизация'
    h1 = 'Авторизация страница эпичного хабра'

    content = {
        'h1': h1,
        'title': title,
        'form': form,
    }

    return render(request, 'userapp/login.html', content)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login:index'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    title = 'Регистрация'
    h1 = 'Регистрация на эпичном хабра'
    content = {
        'h1': h1,
        'title': title,
        'form': form
    }
    return render(request, 'userapp/register.html', content)
