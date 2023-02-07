import pathlib

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import BadRequest
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView

from authapp.forms import RegisterUserForm
from mainapp.services import FileMode


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'authapp/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if settings.DEBUG:
            try:
                context['debug_mode'] = True
                some_file = list(pathlib.Path(settings.BASE_DIR / 'mainapp' / 'management' / 'data').glob('*.txt'))[0]
                with open(
                        file=some_file,
                        mode=FileMode.READ.value,
                        encoding='utf-8'
                ) as fake_user_data_file:
                    context['fake_users_data'] = fake_user_data_file.readlines()
            except IndexError:
                pass

        return context

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        if user.is_moderator:
            return redirect('moderatorapp:moderator_lk')
        if user.is_candidate:
            return redirect('candidateapp:candidate_lk')
        if user.is_company:
            return redirect('companyapp:company_profile')
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
