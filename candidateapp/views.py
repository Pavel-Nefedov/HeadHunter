from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,HttpResponseRedirect

from django.views.generic import UpdateView, DetailView

from candidateapp.models import Candidate
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

# class ShowProfileUpdateView(UpdateView):
#     model = Candidate
#     template_name = 'candidateapp/candidate_update.html'
#
#     def get_context_data(self, *args, **kwargs):
#         # users = Candidate.objects.all()
#         context = super(ShowProfileUpdateView, self).get_context_data(*args, **kwargs)
#         page_user = get_object_or_404(Candidate, id=self.kwargs['pk'])
#         context['page_user'] = page_user
#         return context

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





# update view for details
# def update_view(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     context = {}
#
#     # fetch the object related to passed id
#     obj = get_object_or_404(Candidate, id=id)
#
#     # pass the object as instance in form
#     form = CandidateForm(request.POST or None, instance=obj)
#
#     # save the data from the form and
#     # redirect to detail_view
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/" + id)
#
#     # add form dictionary to context
#     context["form"] = form
#
#     return render(request, "candidate_update.html", context)
