from django.urls import path

from companyapp.views import CompanyK, CompanyLK, VacancySearch, Vacancy




app_name = 'companyapp'

urlpatterns = [
    path('company_profile/<int:pk>/',  CompanyLK.as_view(), name='company_profile'),
    path('company_lk/', CompanyK.as_view(), name='company_lk'),
    path('vacancy_search/',  VacancySearch.as_view(), name='vacancy_search'),
    path('vacancy/<int:pk>/', Vacancy.as_view(), name='vacancy'),
]
