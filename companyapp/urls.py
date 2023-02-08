from django.urls import path

from companyapp.views import (CompanyProfileCreateView,
                              CompanyProfileUpdateView,
                              PartnerCompanyView,
                              ResumeSearch, VacancyCreate, VacancyUpdate,
                              VacancyView, CompProfile, VacanciesList, FormResumeSearch)

app_name = 'companyapp'

urlpatterns = [
    path('company_profile/compprofile/', CompProfile.as_view(), name='company_profile'),
    path('company_profile/create/', CompanyProfileCreateView.as_view(), name='company_create'),
    path('company_profile/update/<int:pk>/', CompanyProfileUpdateView.as_view(), name='company_update'),
    path('comp_vacancies/', VacanciesList.as_view(), name='vac_list'),
    path('comp_vacancies_select/', VacanciesList.as_view(), name='vac_select'),
    # path('comp_vacancies_alert/', VacanciesList.as_view(), name='vac_select'),
    path('vacancy/create/', VacancyCreate.as_view(), name='vacancy_create'),
    path('vacancy/edit/<int:pk>/', VacancyUpdate.as_view(), name='vacancy_edit'),
    path('vacancy/<int:pk>/', VacancyView.as_view(), name='vacancy'),
    path('resume_search/', ResumeSearch.as_view(), name='resume_search'),
    path('form_resume_search/', FormResumeSearch.as_view(), name='form_resume_search'),
    path('favorites/', VacancyView.as_view(), name='favorites'),
    path('partner/<int:pk>/', PartnerCompanyView.as_view(), name='partner'),
]
