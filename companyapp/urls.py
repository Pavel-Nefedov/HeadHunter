from django.urls import path

from companyapp.views import (CompanyK, CompanyLK, Vacancy, VacancyCreate,
                            VacancyUpdate, VacancyView, ResumeSearch)

app_name = 'companyapp'

urlpatterns = [
    path('company_profile/<int:pk>/',  CompanyLK.as_view(), name='company_profile'),
    path('company_lk/', CompanyK.as_view(), name='company_lk'),
    path('vacancy/create/', VacancyCreate.as_view(), name='vacancy_create'),
    path('vacancy/edit/<int:pk>/', VacancyUpdate.as_view(), name='vacancy_edit'),
    path('vacancy/<int:pk>/', VacancyView.as_view(), name='vacancy'),
    path('resume_search/',  ResumeSearch.as_view(), name='resume_search')
]
