from django.views.generic import TemplateView



class CompanyLK(TemplateView):
    template_name = 'companyapp/company.html'


class CompanyK(TemplateView):
    template_name = 'companyapp/company_lk.html'


class VacancySearch(TemplateView):
    template_name = 'companyapp/vacancy_search.html'
