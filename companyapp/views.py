from django.views.generic import TemplateView, DetailView

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, View
from companyapp.forms import CompanyProfileForm
from companyapp.models import CompanyProfile, Vacancy


class CompanyLK(TemplateView):
    template_name = 'companyapp/company.html'


# class CompanyK(TemplateView):
#     template_name = 'companyapp/company_lk.html'


class VacancySearch(TemplateView):
    template_name = 'companyapp/vacancy_search.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['vacancies'] = Vacancy.objects.filter(is_active=True).order_by('-created')[:10]
        return data


### уже есть class Vacancy. Это название модели поэтому переименовал контроллер class Vacancy в class VacancyView
class VacancyView(DetailView):
    template_name = 'companyapp/vacancy.html'
    model = Vacancy

    def get_context_data(self, pk=None, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(pk=pk)
        return context


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
