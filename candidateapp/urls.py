from django.urls import path

# from .views import candidate
from .views import ShowProfilePageView, ShowProfileUpdateView, ShowResumePageView


app_name = 'candidateapp'


urlpatterns = [
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('resume/<int:pk>/', ShowResumePageView.as_view(), name='resume'),

    path('update/<int:pk>/', ShowProfileUpdateView.as_view(), name='update_profile'),

]
