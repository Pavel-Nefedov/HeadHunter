from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages

import sys

from mainapp.models import Article

sys.path.append('../')

from userapp.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


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
            messages.success(request, 'Вы успешно зарегистрировались!')
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


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    title = 'Личный кабинет'
    h1 = 'Личный кабинет на эпичном хабре'
    article_list = Article.objects.filter(author=request.user, deleted_at=None)
    content = {
        'h1': h1,
        'title': title,
        'form': form,
        'article_list': article_list,
    }
    return render(request, 'userapp/profile.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
