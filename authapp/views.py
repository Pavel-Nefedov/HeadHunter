from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.core.exceptions import BadRequest, PermissionDenied
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from authapp.forms import RegisterUserForm


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'authapp/login.html'

    def get_success_url(self):
        return reverse_lazy('authapp:login_success')
    # Тут будет перенаправление в ЛК кандидата или в ЛК работодателя


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'authapp/register.html'

    def form_valid(self, form):

        user = form.save()

        if form.cleaned_data['user_role'] == 'is_company':
            user.is_company = True
            user.save()
            login(self.request, user)
            return redirect('companyapp:company_profile', pk=user.pk)
        elif form.cleaned_data['user_role'] == 'is_candidate':
            user.is_candidate = True
            user.save()
            login(self.request, user)
            return redirect('candidateapp:user_profile', pk=user.pk)
        else:
            raise BadRequest


class SuccessLogin(TemplateView):
    template_name = 'authapp/login_success.html'


class LogoutUser(LogoutView):
    template_name = 'authapp/login.html'
