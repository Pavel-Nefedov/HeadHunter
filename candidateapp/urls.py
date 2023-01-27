from django.urls import path

import candidateapp.views as candidateapp

from .views import (Candidate_Main, FormVacancySearch, ShowProfileUpdateView,
                    ShowResumeDetailView, VacancySearch)

app_name = 'candidateapp'


urlpatterns = [
    # path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    # path('resume/<int:pk>/', ShowResumePageView.as_view(), name='resume'),
    # path('candidate_lk/', CandidateLK.as_view(), name='candidate_lk'),
    # path('update/<int:pk>/', ShowProfileUpdateView.as_view(), name='update_profile'),
    path('user_profile/', candidateapp.candidate_lk, name='user_profile'),
    path('resume/', candidateapp.resume, name='resume'),
    # path('resume_detail/', candidateapp.resume_detail, name='resume_detail'),
    # path('resume/<int:pk>/', ShowResumePageView.as_view(), name='resume'),
    path('resume_detail/<int:pk>/', ShowResumeDetailView.as_view(), name='resume_detail'),
    path('candidate/', Candidate_Main.as_view(), name='candidate_lk'),
    path('update/<int:pk>/', ShowProfileUpdateView.as_view(), name='update_profile'),
    path('vacancy_search/',  VacancySearch.as_view(), name='vacancy_search'),
    path('search/',  FormVacancySearch.as_view(), name='form_vacancy_search'),
]
