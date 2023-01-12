from django.urls import path

from .views import (CandidateLK, ShowProfilePageView, ShowProfileUpdateView,
                    ShowResumePageView)

# from .views import candidate


app_name = 'candidateapp'


urlpatterns = [
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('resume/<int:pk>/', ShowResumePageView.as_view(), name='resume'),
    path('candidate_lk/', CandidateLK.as_view(), name='candidate_lk'),
    path('update/<int:pk>/', ShowProfileUpdateView.as_view(), name='update_profile'),
]
