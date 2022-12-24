from django.urls import path

from companyapp.views import CompanyLK

app_name = 'companyapp'

urlpatterns = [
    path('company_profile/<int:pk>/', CompanyLK.as_view(), name='company_profile'),
]
