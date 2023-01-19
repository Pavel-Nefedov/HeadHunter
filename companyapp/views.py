from django.views.generic import TemplateView, DetailView

from companyapp.models import Vacancy


class CompanyLK(TemplateView):
    template_name = 'companyapp/company.html'


class CompanyK(TemplateView):
    template_name = 'companyapp/company_lk.html'


class VacancySearch(TemplateView):
    template_name = 'companyapp/vacancy_search.html'

class Vacancy(DetailView):
    template_name = 'companyapp/vacancy.html'
    model = Vacancy
