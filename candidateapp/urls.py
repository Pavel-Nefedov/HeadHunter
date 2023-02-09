from django.urls import path

import candidateapp.views as candidateapp

from .views import (FormVacancySearch, ResumeCreateView, ResumeDeleteView,
                    ResumeUpdate, ShowProfileUpdateView, ShowResumeDetailView,
                    VacancySearch)

app_name = 'candidateapp'


urlpatterns = [
    # path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    # path('resume/<int:pk>/', ShowResumePageView.as_view(), name='resume'),
    # path('candidate_lk/', CandidateLK.as_view(), name='candidate_lk'),
    path('candidate_update/<int:pk>/', ShowProfileUpdateView.as_view(), name='candidate_update'),
    path('user_profile/', candidateapp.candidate_lk, name='user_profile'),

    # path('resume/', ResumeList.as_view(), name='resume'),
    path('resume/', candidateapp.resume, name='resume'),
    # path('resume_update/<int:pk>/', candidateapp.resume_update, name='resume_update'),
    path('resume_update/<int:pk>/', ResumeUpdate.as_view(), name='resume_update'),
    # path('resume_create/', candidateapp.resume_create, name='resume_create'),
    path('resume_create/', ResumeCreateView.as_view(), name='resume_create'),
    path('resume_delete/<int:pk>/', ResumeDeleteView.as_view(), name='resume_delete'),
    # path('resume/<int:pk>/', ShowResumePageView.as_view(), name='resume'),
    path('resume_detail/<int:pk>/', ShowResumeDetailView.as_view(), name='resume_detail'),
    # path('candidate/', CandidateMain.as_view(), name='candidate_lk'),
    # path('update/<int:pk>/', ShowProfileUpdateView.as_view(), name='update_profile'),
    path('vacancy_search/', VacancySearch.as_view(), name='vacancy_search'),
    path('search/', FormVacancySearch.as_view(), name='form_vacancy_search'),
]
