from django.urls import path

from companyapp.views import (CompanyProfileUpdateView, CompanyProfileCreateView,
                              CompanyProfileView, VacancyCreate,EmptyCompanyProfile,
                              VacancyUpdate, VacancyView, ResumeSearch, PartnerCompanyView)

app_name = 'companyapp'

urlpatterns = [

    path('company_profile/<int:pk>/', CompanyProfileView.as_view(), name='company_profile'),
    path('company_profile/empty/', EmptyCompanyProfile.as_view(), name='empty_profile'),
    path('company_profile/create/', CompanyProfileCreateView.as_view(), name='company_create'),
    path('company_profile/update/<int:pk>/', CompanyProfileUpdateView.as_view(), name='company_update'),
    path('vacancy/create/', VacancyCreate.as_view(), name='vacancy_create'),
    path('vacancy/edit/<int:pk>/', VacancyUpdate.as_view(), name='vacancy_edit'),
    path('vacancy/<int:pk>/', VacancyView.as_view(), name='vacancy'),
    path('resume_search/',  ResumeSearch.as_view(), name='resume_search'),
    path('favorites/',  VacancyView.as_view(), name='favorites'),
    path('partner/<int:pk>/', PartnerCompanyView.as_view(), name='partner'),
]
