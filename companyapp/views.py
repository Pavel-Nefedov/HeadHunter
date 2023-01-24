from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DetailView, TemplateView,
                                  UpdateView, View)

from companyapp.forms import CompanyProfileForm, VacancyForm
from companyapp.models import CompanyProfile, Vacancy
from candidateapp.models import Resume


class CompanyLK(TemplateView):
    template_name = 'companyapp/company.html'


# class CompanyK(TemplateView):
#     template_name = 'companyapp/company_lk.html'


# class VacancySearch(TemplateView):
#     template_name = 'companyapp/vacancy_search.html'
#     model = Vacancy
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         data['vacancies'] = Vacancy.objects.filter(is_active=True).order_by('-created')[:10]
#         return data


### уже есть class Vacancy. Это название модели поэтому переименовал контроллер class Vacancy в class VacancyView
class VacancyView(DetailView):
    template_name = 'companyapp/vacancy.html'
    model = Vacancy

    def get_context_data(self, pk=None, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(pk=pk)
        context['user'] = self.request.user
        context['company'] = self.object.company
        return context


class VacancyCreate(LoginRequiredMixin, CreateView):
    template_name = 'companyapp/vacancy_create.html'
    model = Vacancy
    fields = ['vacancy_name', 'city', 'duties_description', 'requirements_description', 'work_conditions', 'salary_min',
              'salary_max', 'currency', 'is_for_disabled', 'is_full_day', 'is_intern']
    form_model = VacancyForm

    def get_success_url(self):
        return reverse('companyapp:vacancy', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.company = CompanyProfile.objects.get(user=self.request.user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['company'] = CompanyProfile.objects.get(user=self.request.user)
        return data


class VacancyUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'companyapp/vacancy_edit.html'
    model = Vacancy
    fields = ['vacancy_name', 'city', 'duties_description', 'requirements_description', 'work_conditions', 'salary_min',
              'salary_max', 'currency', 'is_for_disabled', 'is_full_day', 'is_intern']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['company'] = CompanyProfile.objects.get(user=self.request.user)
        return data

    def get_success_url(self):
        return reverse('companyapp:vacancy', kwargs={'pk': self.object.id})


class CompanyK(View):

    def get(self, request):
        if request.method == 'POST':
            form = CompanyProfileForm(data=request.POST, files=request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('company_lk'))
        else:
            form = CompanyProfileForm(instance=request.user)

        context = {
            'title': 'Профиль',
            'form': form,
        }
        return render(request, 'companyapp/company_lk.html', context)


class ResumeSearch(TemplateView):
    template_name = 'companyapp/resume_search.html'
    model = Resume

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # data['resume'] = Resume.objects.filter().order_by('-created')[:10]
        return data

# def CompanyK(request):
#     if request.method == 'POST':
#         form = CompanyProfileForm(data=request.POST, files=request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('company_lk'))
#     else:
#         form = CompanyProfileForm(instance=request.user)
#
#     context = {
#         'title': 'Профиль',
#         'form': form,
#     }
#     return render(request, 'companyapp/company_lk.html', context)

