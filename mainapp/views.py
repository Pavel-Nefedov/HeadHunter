from django.views.generic import ListView, TemplateView

from companyapp.models import CompanyProfile, Vacancy
from mainapp.models import News
from messageapp.models import Chat, ChatManager


class Index(TemplateView):
    paginate_by = 5
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['news'] = News.objects.all().order_by('-date')[:3]
        data['companys'] = CompanyProfile.objects.all().order_by('-pk')[:4]
        data['vacancies'] = Vacancy.objects.filter(is_active=True).order_by('-created')[:5]
        return data


class PortalRules(TemplateView):
    paginate_by = 5
    template_name = 'mainapp/portal_rules.html'


class AllNews(TemplateView):
    template_name = 'mainapp/all_news.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['news'] = News.objects.all().order_by('-date')
        return data
