from django.views.generic import TemplateView, DetailView

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, CreateView,View
from companyapp.forms import CompanyProfileForm
from companyapp.models import CompanyProfile, Vacancy


class CompanyLK(TemplateView):
    template_name = 'companyapp/company.html'


# class CompanyK(TemplateView):
#     template_name = 'companyapp/company_lk.html'


class VacancySearch(TemplateView):
    template_name = 'companyapp/vacancy_search.html'

class Vacancy(DetailView):
    template_name = 'companyapp/vacancy.html'
    model = Vacancy


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