from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.views.generic import DetailView, TemplateView, UpdateView, ListView

from authapp.models import HHUser
from candidateapp.models import Candidate, Resume
from authapp.models import HHUser
from django.contrib.auth.decorators import login_required
from companyapp.models import Vacancy

# from candidateapp.forms import CandidateForm

class Candidate_Main(TemplateView):
    template_name = 'candidateapp/candidate_lk.html'

class Candidate_Main(TemplateView):
    template_name = 'candidateapp/candidate.html'

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
    resume_items = Resume.objects.all()
    candidate_items = Candidate.objects.filter(user=request.user).select_related()

    context = {
        'title': title,
        'resume_items': resume_items,
        'candidate_items': candidate_items,
    }
    return render(request, 'candidateapp/resume.html', context)


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
