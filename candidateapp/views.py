from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,HttpResponseRedirect

from django.views.generic import UpdateView, DetailView

from candidateapp.models import Candidate, Resume
from candidateapp.forms import CandidateForm


class ShowProfilePageView(DetailView):
    model = Candidate
    template_name = 'candidateapp/candidate.html'

    def get_context_data(self, *args, **kwargs):
        # users = Candidate.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Candidate, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


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

class ShowResumePageView(DetailView):
    model = Resume
    template_name = 'candidateapp/resume.html'

    def get_context_data(self, *args, **kwargs):
        # users = Candidate.objects.all()
        context = super(ShowResumePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Resume, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context