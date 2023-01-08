from django.shortcuts import render
from django.views.generic import TemplateView
from companyapp.models import Vacancy

from mainapp.models import News

from mainapp.models import News


class Index(TemplateView):
    template_name = 'mainapp/index.html'
    extra_context = {'vacancies': Vacancy.objects.all().order_by('-created')[:5]}

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['news'] = News.objects.all().order_by('-pk')[:3]
        return data
