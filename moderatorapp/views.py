from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from candidateapp.models import Resume
from companyapp.models import CompanyProfile, Vacancy
from mainapp.mixins import IsModeratorCheckMixin


@method_decorator(login_required, name='dispatch')
class ModeratorLkIndex(IsModeratorCheckMixin, TemplateView):
    template_name = 'moderatorapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_for_moderation'] = Resume.objects.filter(is_moderated=False)
        context['company_profiles_for_moderation'] = CompanyProfile.objects.filter(is_moderated=False)
        context['vacancy_for_moderation'] = Vacancy.objects.filter(is_moderated=False)
        return context


@method_decorator(login_required, name='dispatch')
class ModeratorLkResume(IsModeratorCheckMixin, TemplateView):
    template_name = 'moderatorapp/resume_moderate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_for_moderation'] = Resume.objects.filter(is_moderated=False)
        context['company_profiles_for_moderation'] = CompanyProfile.objects.filter(is_moderated=False)
        context['vacancy_for_moderation'] = Vacancy.objects.filter(is_moderated=False)
        return context


@method_decorator(login_required, name='dispatch')
class ModeratorLkCompanyProfile(IsModeratorCheckMixin, TemplateView):
    template_name = 'moderatorapp/company_profile_moderate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_for_moderation'] = Resume.objects.filter(is_moderated=False)
        context['company_profiles_for_moderation'] = CompanyProfile.objects.filter(is_moderated=False)
        context['vacancy_for_moderation'] = Vacancy.objects.filter(is_moderated=False)
        return context


@method_decorator(login_required, name='dispatch')
class ModeratorLkVacancy(IsModeratorCheckMixin, TemplateView):
    template_name = 'moderatorapp/vacancy_moderate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_for_moderation'] = Resume.objects.filter(is_moderated=False)
        context['company_profiles_for_moderation'] = CompanyProfile.objects.filter(is_moderated=False)
        context['vacancy_for_moderation'] = Vacancy.objects.filter(is_moderated=False)
        return context
