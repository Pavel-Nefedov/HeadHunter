from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView

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


class ShowProfilePageView(DetailView):
    model = Candidate
    template_name = 'candidateapp/candidate.html'

    def get_context_data(self, *args, **kwargs):
        # users = Candidate.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Candidate, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
