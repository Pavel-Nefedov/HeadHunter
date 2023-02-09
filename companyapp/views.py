from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  TemplateView, UpdateView, View, ListView)

from candidateapp.models import Resume
from companyapp.forms import CompanyProfileForm, VacancyForm
from companyapp.models import CompanyProfile, Vacancy


class CompProfile(ListView):
    template_name = 'companyapp/comp_profile.html'
    model = CompanyProfile

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=None, **kwargs)
        context['profile'] = CompanyProfile.objects.filter(user=self.request.user)
        context['user'] = self.request.user
        return context


class CompanyProfileCreateView(LoginRequiredMixin, CreateView):
    model = CompanyProfile
    template_name = 'companyapp/company_lk.html'
    # success_url = reverse_lazy('companyapp:company_profile')
    form_class = CompanyProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('companyapp:company_profile')


# class CompanyProfileDeleteView(LoginRequiredMixin,DeleteView):
#     model = CompanyProfile
#     template_name = 'companyapp/company_lk.html'
#     success_url = reverse_lazy('companyapp:company_profile')
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.is_active = False
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())



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
    template_name = 'companyapp/company_profile_upd_del.html'
    success_url = reverse_lazy('companyapp:company_profile')
    form_class = CompanyProfileForm

    def get_context_data(self, **kwargs):
        context = super(CompanyProfileUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Company profile update'
        return context


class VacanciesList(ListView):
    template_name = 'companyapp/company_vacancies_list.html'
    model = Vacancy

    #
    def dispatch(self, request, *args, **kwargs):
        return super(VacanciesList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, pk=None, **kwargs):
        context = super(VacanciesList, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['company'] = CompanyProfile.objects.get(user=self.request.user)
        context['vacancies'] = Vacancy.objects.filter(company_id=pk)
        return context


# уже есть class Vacancy. Это название модели поэтому переименовал контроллер class Vacancy в class VacancyView
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
        data['company'] = CompanyProfile.objects.filter(user=self.request.user)
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

class VacanciesSelect(ListView):
    template_name = 'companyapp/company_vacancies_select.html'
    model = Vacancy

    #
    def dispatch(self, request, *args, **kwargs):
        return super(VacanciesList, self).dispatch(request, *args, **kwargs)
        
    def get_context_data(self, pk=None, **kwargs):
        context = super(VacanciesList, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['company'] = CompanyProfile.objects.get(user=self.request.user)
        context['vacancies'] = Vacancy.objects.filter(company_id=pk)
        if context['vacancies']:   
            return context


#                 if queryset:
#             return super(VacanciesList, self).dispatch(request, *args, **kwargs)
#         else:
#             return render(request, 'companyapp/vacancy_alert.html')

#    queryset = Resume.objects.filter(candidate_id=request.user)

#     if queryset:
#         return render(request, 'candidateapp/resume_select.html', context)
#     else:
#         return render(request, 'candidateapp/resume_alert.html')

        # if context['company']:
        #     return context
        # else:
        #     return render(request, 'candidateapp/vacancy_alert.html')

    
    # def vacancy_alert(request):
    #     queryset = Vacancy.objects.filter(company_id=pk)
    #     if not queryset:
    #         return render(request, 'candidateapp/vacancy_alert.html')



class ResumeSearch(TemplateView):
    template_name = 'companyapp/resume_search.html'
    model = Resume

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # data['resume'] = Resume.objects.filter().order_by('-created')[:10]
        data["resumes"] = Resume.objects.all()
        return data


class FormResumeSearch(ListView):
    template_name = 'companyapp/form_resume_search.html'
    paginate_by = 10
    model = Resume

    def get_queryset(self):
        search_text = self.request.GET.get('search_text')

        if search_text:
            search_queryset = Resume.objects.filter(
                Q(level__contains=search_text) |
                Q(specialization__contains=search_text) |
                Q(skills__icontains=search_text) |
                Q(responsibilities__icontains=search_text)).select_related()
        else:
            search_queryset = Resume.objects.all().select_related()

        return search_queryset


class Favorites(TemplateView):
    template_name = 'companyapp/favorites.html'
    model = Resume

    def favorites_list(request):
        context = {
            "favorites_list": request.session.get('favorites'),
        }
        return render(request, 'favorites', context=context)


class PartnerCompanyView(DetailView):
    template_name = 'companyapp/partner_company.html'
    model = CompanyProfile

    def get_context_data(self, pk=None, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['company'] = CompanyProfile.objects.filter(pk=pk)
        return context
