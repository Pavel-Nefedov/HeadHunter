from django.urls import path

# from .views import candidate
from .views import ShowProfilePageView, CandidateLK

app_name = 'candidateapp'

urlpatterns = [
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('candidate_lk/', CandidateLK.as_view(), name='candidate_lk'),
]
