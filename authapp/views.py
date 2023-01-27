from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import BadRequest, PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView

from authapp.forms import RegisterUserForm
from authapp.models import HHUser


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'authapp/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        if user.is_candidate:
            return redirect('candidateapp:user_profile')
        if user.is_company:
            return redirect('companyapp:company_lk')
        if user.is_superuser:
            return redirect('/admin', pk=user.pk)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'authapp/register.html'

    def form_valid(self, form):

        user = form.save()

        if form.cleaned_data['user_role'] == 'is_company':
            user.is_company = True
            user.save()
            login(self.request, user)
            return redirect('companyapp:resume_search')
        elif form.cleaned_data['user_role'] == 'is_candidate':
            user.is_candidate = True
            user.save()
            login(self.request, user)
            return redirect('candidateapp:vacancy_search')
        else:
            raise BadRequest


class SuccessLogin(TemplateView):
    template_name = 'authapp/login_success.html'


class LogoutUser(LogoutView):
    next_page = '/auth/login'

