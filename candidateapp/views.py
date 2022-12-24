from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from authapp.models import HHUser
from candidateapp.models import Candidate


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

