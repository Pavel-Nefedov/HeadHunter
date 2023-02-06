from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from authapp.models import HHUser
from candidateapp.forms import CandidateForm,  ContactInfoForm, PositionAndSalaryForm, WorkExperienceForm, \
    EducationForm, AdvancedTrainingForm, ResumeForm
from candidateapp.models import Candidate, ContactInfo, PositionAndSalary, WorkExperience, Education, \
    AdvancedTraining, Resume
from companyapp.models import Vacancy

# from candidateapp.forms import CandidateForm


class CandidateMain(TemplateView):
    template_name = 'candidateapp/candidate_lk.html'


# class ShowProfilePageView(TemplateView):
#     template_name = 'candidateapp/candidate.html'


@login_required
def candidate_lk(request):
    title = 'candidate'
    candidate_items = Candidate.objects.filter(user=request.user).select_related()

    context = {
        'title': title,
        'candidate_items': candidate_items,

    }
    return render(request, 'candidateapp/candidate_lk.html', context)


class ShowProfileUpdateView(UpdateView):
    model = Candidate
    template_name = 'candidateapp/candidate_update.html'
    fields = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "search_area",
    ]


class ShowResumeDetailView(DetailView):
    model = Resume
    template_name = 'candidateapp/resume_detail.html'

    def get_context_data(self, pk=None, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['resume'] = Resume.objects.all()
        context['user'] = self.request.user
        return context


# @login_required
# def resume_detail(request):
#     title = 'развернутое резюме'
#     resume_items = Resume.objects.all()
#
#     context = {
#         'title': title,
#         'resume_items': resume_items,
#     }
#     return render(request, 'candidateapp/resume_detail.html', context)


@login_required
def resume(request):
    title = 'резюме'
    # resume_items = Resume.objects.all()
    resume_items = Resume.objects.all(), ContactInfo.objects.all()
    candidate_items = Candidate.objects.filter(user=request.user).select_related()

    context = {
        'title': title,
        'resume_items': resume_items,
        'candidate_items': candidate_items,
    }
    return render(request, 'candidateapp/resume.html', context)




# @login_required
# def resume_create(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         surname = request.POST['surname']
#         patronymic = request.POST['patronymic']
#         birthday = request.POST['birthday']
#         city = request.POST['city']
#
#         contact_info = ContactInfo.objects.create(name=name,
#                                             surname=surname,
#                                             patronymic=patronymic,
#                                             birthday=birthday, city=city,
#                                             )
#         contact_info.save()
#         alert = True
#         return render(request, 'candidateapp/resume.html', {'alert': alert})
#     return render(request, 'candidateapp/resume_create.html')


@login_required()
def resume_create(request):
    form1 = ContactInfoForm()
    form2 = PositionAndSalaryForm()
    form3 = WorkExperienceForm()
    form4 = EducationForm()
    form5 = AdvancedTrainingForm()

    if request.method == 'POST':
        form1 = ContactInfoForm(request.POST)
        form2 = PositionAndSalaryForm(request.POST)
        form3 = WorkExperienceForm(request.POST)
        form4 = EducationForm(request.POST)
        form5 = AdvancedTrainingForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            form1.save()
            form2.save()
            form3.save()
            form4.save()
            form5.save()
            return redirect('candidate:resume')

    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
    }
    return render(request, 'candidateapp/resume_create.html', context)


@login_required()
def resume_update(request, pk):
    if request.method == 'POST':
        form1 = ContactInfoForm(request.POST, instance='form1')
        form2 = PositionAndSalaryForm(request.POST, instance='form2')
        form3 = WorkExperienceForm(request.POST, instance='form3')
        form4 = EducationForm(request.POST, instance='form4')
        form5 = AdvancedTrainingForm(request.POST, instance='form5')
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            form1.save()
            form2.save()
            form3.save()
            form4.save()
            form5.save()
            return reverse('candidate:resume')

    form1 = ContactInfoForm()
    form2 = PositionAndSalaryForm()
    form3 = WorkExperienceForm()
    form4 = Education()
    form5 = AdvancedTrainingForm()
    data = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
    }
    return render(request, 'candidateapp/resume_update.html', data)


@login_required()
def resume_delete(request, pk):
    title = 'Удаление резюме'
    resume = get_object_or_404(Resume, pk=pk)

    if request.method == 'POST':
        resume.is_active = False
        resume.save()
        return HttpResponseRedirect(reverse('candidate:resume'))

    content = {'title': title, 'resume_to_delete': resume}

    return render(request, 'candidateapp/resume_delete.html', content)



# class ResumeDeleteView(LoginRequiredMixin, DeleteView):
#     model = Resume
#     template_name = 'candidateapp/resume_delete.html'
#     success_url = reverse_lazy('candidate:resume')
#
#     def delete(self, request, *arg, **kwargs):
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         self.object.is_active = False
#         self.object.save()
#         return HttpResponseRedirect(success_url)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "Удаление резюме"
#         return context


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





class ResumeView(DetailView):
    template_name = 'candidateapp/resume.html'
    model = Resume

    def get_context_data(self, request, pk=None, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['title'] = Resume.objects.filter(pk=pk)
        context['resume_items'] = Resume.objects.all()
        context['candidate_items'] = Candidate.objects.filter(user=request.user).select_related()
        return context



# class ResumeCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'candidateapp/resume_create.html'
#     model = Resume
#     fields = ['contact_info', 'position_and_salary',
#               'work_experience', 'education', 'advanced_training']
#     form_model = ResumeForm
#
#     def get_success_url(self):
#         return reverse('candidateapp:resume')
#
#     # def form_valid(self, form):
#     #     form.instance.company = CompanyProfile.objects.get(user=self.request.user)
#     #     return super().form_valid(form)
#     #
#     # def get_context_data(self, **kwargs):
#     #     data = super().get_context_data(**kwargs)
#     #     data['company'] = CompanyProfile.objects.get(user=self.request.user)
#     #     return data
#
#
# class ResumeUpdate(LoginRequiredMixin, UpdateView):
#     template_name = 'candidateapp/resume_update.html'
#     model = Resume
#     fields = ['contact_info', 'position_and_salary',
#               'work_experience', 'education', 'advanced_training']
#     form_model = ResumeForm
#
#     # def get_context_data(self, **kwargs):
#     #     data = super().get_context_data(**kwargs)
#     #     data['company'] = CompanyProfile.objects.get(user=self.request.user)
#     #     return data
#
#     def get_success_url(self):
#         return reverse('candidateapp:resume')