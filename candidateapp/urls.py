from django.urls import path

# from .views import candidate
from .views import ShowProfilePageView

app_name = 'candidateapp'

# urlpatterns = [
#     path('', candidate, name='index'),
# ]

urlpatterns = [path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),

               ]
