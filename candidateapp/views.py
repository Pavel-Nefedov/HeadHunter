from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from authapp.models import HHUser
from authapp.forms import RegisterUserForm
from candidateapp.forms import ResumeForm
from candidateapp.models import Resume
from companyapp.models import Vacancy

""" Блок кандидата"""
# @login_required
# def candidate_lk(request):
#     title = 'candidate'
#     user = request.user
#
#     context = {
#         'title': title,
#         'user': user,
#
#     }
#     return render(request, 'candidateapp/candidate_lk.html', context)


class CandidateMain(ListView):
    template_name = 'candidateapp/candidate_lk.html'
    model = HHUser

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=None, **kwargs)
        context['profile'] = HHUser.objects.filter(username=self.request.user)
        context['user'] = self.request.user
        return context


class ShowProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = HHUser
    template_name = 'candidateapp/candidate_update.html'
    fields = [
        'username',
        'first_name',
        'last_name',
        'patronymic',
        'birthday',
        'email',
        'city'
    ]
    # form_class = RegisterUserForm

    def get_context_data(self, **kwargs):
        context = super(ShowProfileUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Candidate profile update'
        return context

    def get_success_url(self):
        return reverse('candidate:user_profile')


""" Блок резюме!!!!!!!!!!"""


# @login_required
# def resume(request):
#     title = 'резюме'
#     resume_items = Resume.objects.filter(candidate=request.user)
#
#     context = {
#         'title': title,
#         'resume_items': resume_items,
#     }
#     return render(request, 'candidateapp/resume.html', context)


class ResumeView(ListView):
    template_name = 'candidateapp/resume.html'
    model = Resume
    form_model = ResumeForm

    def get_context_data(self, pk=None, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)
        context['resume_items'] = Resume.objects.filter(candidate=self.request.user)
        return context


class ShowResumeDetailView(DetailView):
    model = Resume
    template_name = 'candidateapp/resume_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume'] = Resume.objects.get(pk=self.kwargs['pk'])
        if self.request.user.is_company:
            context['company_vacancy'] = Vacancy.objects.filter(
                company__pk=self.request.user.pk,
            )
        return context


class ResumeCreateView(CreateView):
    model = Resume
    template_name = 'candidateapp/resume_create.html'
    fields = [
            'is_moderated',
            'moving',
            'business_trips',
            'desired_position',
            'salary',
            'busyness',
            'work_schedule',
            'getting_started',
            'end_work',
            'working',
            'organization',
            'post',
            'responsibilities',
            'skills',
            'about_me',
            'level',
            'educational_institution',
            'faculty',
            'specialization',
            'year_graduation',
            'course_name',
            'organization_conducted',
            'specialization_course',
            'year_graduation_course',
            'is_draft'
        ]
    form_model = ResumeForm

    def get_success_url(self):
        return reverse('candidate:resume')

    def form_valid(self, form):
        form.instance.candidate = HHUser.objects.get(username=self.request.user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['candidate'] = Resume.objects.filter(candidate=self.request.user)
        return data


class ResumeUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'candidateapp/resume_update.html'
    model = Resume
    fields = ['is_moderated',
            'moving',
            'business_trips',
            'desired_position',
            'salary',
            'busyness',
            'work_schedule',
            'getting_started',
            'end_work',
            'working',
            'organization',
            'post',
            'responsibilities',
            'skills',
            'about_me',
            'level',
            'educational_institution',
            'faculty',
            'specialization',
            'year_graduation',
            'course_name',
            'organization_conducted',
            'specialization_course',
            'year_graduation_course',
            'is_draft']

    def get_success_url(self):
        return reverse('candidateapp:resume')


class ResumeDeleteView(LoginRequiredMixin, DeleteView):
    model = Resume
    template_name = 'candidateapp/resume_delete.html'
    success_url = reverse_lazy('candidate:resume')

    def delete(self, request, *arg, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Удаление резюме"
        return context


def resume_select(request):
    title = 'выбор резюме'
    resume_items = Resume.objects.filter(candidate=request.user)

    context = {
        'title': title,
        'resume_items': resume_items,
    }

    queryset = Resume.objects.filter(candidate_id=request.user)

    if queryset:
        return render(request, 'candidateapp/resume_select.html', context)
    else:
        return render(request, 'candidateapp/resume_alert.html')


def resume_alert(request):
    title = 'предупреждение по отсутствию резюме'
    return render(request, 'candidateapp/resume_alert.html')


"""Блок поиска вакансий"""


class VacancySearch(TemplateView):
    template_name = 'candidateapp/vacancy_search.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['vacancies'] = Vacancy.objects.filter(is_active=True).order_by('-created')[:10]
        if self.request.user.is_candidate:
            data['candidate_resume'] = Resume.objects.filter(
                candidate__pk=self.request.user.pk,
                is_moderated=True,
                is_draft=False
            )
        return data


class FormVacancySearch(ListView):
    template_name = 'candidateapp/form_vacancy_search.html'
    paginate_by = 10
    model = Vacancy

    def get_queryset(self):
        search_text = self.request.GET.get('search_text')

        if search_text:
            search_queryset = Vacancy.objects.filter(
                Q(company__company_name__contains=search_text) | Q(vacancy_name__contains=search_text)).select_related()
        else:
            search_queryset = Vacancy.objects.all().select_related()

        return search_queryset
