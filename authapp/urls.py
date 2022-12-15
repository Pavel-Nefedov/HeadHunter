from django.urls import path

from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
]
