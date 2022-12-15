from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView


class Login(TemplateView):
    template_name = 'authapp/login.html'
