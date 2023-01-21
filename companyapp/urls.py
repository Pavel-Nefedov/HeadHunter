from django.urls import path

from companyapp.views import CompanyK, CompanyLK, VacancySearch, Vacancy, VacancyCreate, VacancyUpdate, VacancyView

app_name = 'companyapp'

urlpatterns = [
    path('company_profile/<int:pk>/',  CompanyLK.as_view(), name='company_profile'),
    path('company_lk/', CompanyK.as_view(), name='company_lk'),
    path('vacancy_search/',  VacancySearch.as_view(), name='vacancy_search'),
    path('vacancy/create/', VacancyCreate.as_view(), name='vacancy_create'),
    path('vacancy/edit/<int:pk>/', VacancyUpdate.as_view(), name='vacancy_edit'),
    path('vacancy/<int:pk>/', VacancyView.as_view(), name='vacancy'),
]
