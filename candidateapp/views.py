from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView

from authapp.models import HHUser
from candidateapp.models import Candidate
from companyapp.models import Vacancy


#
# def candidate(request):
#     title = 'Личный кабинет'
#     candidate = Candidate.objects.all()
#
#     context = {
#         'title': title,
#         'candidate': candidate,
#     }
#     return render(request, 'candidateapp/candidate.html', context)


class ShowProfilePageView(TemplateView):
    template_name = 'candidateapp/candidate.html'



class CandidateLK(TemplateView):
    template_name = 'candidateapp/candidate_lk.html'
