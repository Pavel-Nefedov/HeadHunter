from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  TemplateView, UpdateView, View, ListView)
from django.db.models import Q
from candidateapp.models import Resume
from companyapp.forms import CompanyProfileForm, VacancyForm
from companyapp.models import CompanyProfile, Vacancy


class EmptyCompanyProfile(TemplateView):
    template_name = 'companyapp/empty_profile.html'


class CompanyProfileView(DetailView):
    template_name = 'companyapp/company_profile_view.html'
    model = CompanyProfile

    def get_context_data(self, pk=None, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['profile'] = CompanyProfile.objects.filter(pk=pk)
        context['user'] = self.request.user
        return context


class CompanyProfileCreateView(LoginRequiredMixin, CreateView):
    model = CompanyProfile
    template_name = 'companyapp/company_lk.html'
    # success_url = reverse_lazy('companyapp:company_profile')
    form_class = CompanyProfileForm

    def get_success_url(self):
        return reverse('companyapp:company_profile', kwargs={'pk': self.object.id})


# class CompanyProfileDeleteView(LoginRequiredMixin,DeleteView):
#     model = CompanyProfile
#     template_name = 'companyapp/company_lk.html'
#     success_url = reverse_lazy('companyapp:company_profile')
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.is_active = False
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())


class CompanyProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CompanyProfile
    template_name = 'companyapp/company_lk.html'
    success_url = reverse_lazy('companyapp:company_profile')
    form_class = CompanyProfileForm

    def get_context_data(self, **kwargs):
        context = super(CompanyProfileUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Company profile update'
        return context


class VacancyView(DetailView):
    template_name = 'companyapp/vacancy.html'
    model = Vacancy

    def get_context_data(self, pk=None, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(pk=pk)
        context['user'] = self.request.user
        context['company'] = self.object.company
        return context


class VacancyCreate(LoginRequiredMixin, CreateView):
    template_name = 'companyapp/vacancy_create.html'
    model = Vacancy
    fields = ['vacancy_name', 'city', 'duties_description', 'requirements_description', 'work_conditions', 'salary_min',
              'salary_max', 'currency', 'is_for_disabled', 'is_full_day', 'is_intern']
    form_model = VacancyForm

    def get_success_url(self):
        return reverse('companyapp:vacancy', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.company = CompanyProfile.objects.get(user=self.request.user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['company'] = CompanyProfile.objects.get(user=self.request.user)
        return data


class VacancyUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'companyapp/vacancy_edit.html'
    model = Vacancy
    fields = ['vacancy_name', 'city', 'duties_description', 'requirements_description', 'work_conditions', 'salary_min',
              'salary_max', 'currency', 'is_for_disabled', 'is_full_day', 'is_intern']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['company'] = CompanyProfile.objects.get(user=self.request.user)
        return data

    def get_success_url(self):
        return reverse('companyapp:vacancy', kwargs={'pk': self.object.id})


class ResumeSearch(TemplateView):
    template_name = 'companyapp/resume_search.html'
    model = Resume

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        #data['resumes'] = Resume.objects.filter().order_by('candidate_id')[:10] ### Вот так тоже ок
        data["resume"] = Resume.objects.all()
        return data


# class CompanyProfileView(DetailView):
#     template_name = 'companyapp/company_profile_view.html'
#     model = CompanyProfile
#
#     def get_context_data(self, pk=None, **kwargs):
#         context = super(DetailView, self).get_context_data(**kwargs)
#         context['profile'] = CompanyProfile.objects.filter(pk=pk)
#         context['user'] = self.request.user
#         return context


class Favorites(TemplateView):
    template_name = 'companyapp/favorites.html'
    model = Resume

    def favorites_list(request):
        context = {
            "favorites_list": request.session.get('favorites'),
        }
        return render(request, 'favorites', context=context)


# def CompanyK(request):
#     if request.method == 'POST':
#         form = CompanyProfileForm(data=request.POST, files=request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('company_lk'))
#     else:
#         form = CompanyProfileForm(instance=request.user)
#
#     context = {
#         'title': 'Профиль',
#         'form': form,
#     }
#     return render(request, 'companyapp/company_lk.html', context)


class PartnerCompanyView(DetailView):
    template_name = 'companyapp/partner_company.html'
    model = CompanyProfile

    def get_context_data(self, pk=None, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['company'] = CompanyProfile.objects.filter(pk=pk)
        return context
