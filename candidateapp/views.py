from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from authapp.forms import RegisterUserForm
from authapp.models import HHUser
from candidateapp.forms import ResumeForm
from candidateapp.models import Resume
from companyapp.models import Vacancy

# class CandidateMain(TemplateView):
#     template_name = 'candidateapp/candidate_lk.html'

""" Блок кандидата"""


@login_required
def candidate_lk(request):
    title = 'candidate'
    user = request.user

    context = {
        'title': title,
        'user': user,

    }
    return render(request, 'candidateapp/candidate_lk.html', context)


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

    def get_success_url(self):
        return reverse('candidate:user_profile')


""" Блок резюме!!!!!!!!!!"""


# class ResumeList(ListView):
#     template_name = 'candidateapp/resume.html'
#     model = Resume
#
#     #
#     def dispatch(self, request, *args, **kwargs):
#         return super(ResumeList, self).dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, pk=None, *args, **kwargs):
#         context = super(ResumeList, self).get_context_data(**kwargs)
#         context['user'] = self.request.user
#         context['candidate'] = Resume.objects.filter(user=self.user.id)
#         # context['candidate'] = Resume.objects.get(candidate=self.request.user)
#         # context['resume'] = Resume.objects.filter(candidate_id=pk)
#         return context


@login_required
def resume(request):
    title = 'резюме'
    resume_items = Resume.objects.filter(candidate=request.user)

    context = {
        'title': title,
        'resume_items': resume_items,
    }
    return render(request, 'candidateapp/resume.html', context)


class ShowResumeDetailView(DetailView):
    model = Resume
    template_name = 'candidateapp/resume_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume'] = Resume.objects.get(pk=self.kwargs['pk'])
        return context


class ResumeCreateView(CreateView):
    model = Resume
    template_name = 'candidateapp/resume_create.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('candidate:resume')


class ResumeUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'candidateapp/resume_update.html'
    model = Resume
    fields = '__all__'
    form_model = ResumeForm

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
    # resume_items = Resume.objects.all()
    # resume_items = Resume.objects.filter(candidate=request.user)
    # candidate_items = Candidate.objects.filter(user=request.user).select_related()

    # context = {
    #     'title': title,
    #     'resume_items': resume_items,
    # }

    return render(request, 'candidateapp/resume_alert.html')
    
    
    # model = Resume
    # template_name = 'candidateapp/resume_select.html'
    # success_url = reverse_lazy('candidate:resume_select')

    # def delete(self, request, *arg, **kwargs):
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.is_active = False
    #     self.object.save()
    #     return HttpResponseRedirect(success_url)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = "Удаление резюме"
    #     return context

"""Блок поиска вакансий"""


class VacancySearch(TemplateView):
    template_name = 'candidateapp/vacancy_search.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['vacancies'] = Vacancy.objects.filter(is_active=True).order_by('-created')[:10]
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
