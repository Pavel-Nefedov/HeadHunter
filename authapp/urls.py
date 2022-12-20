from django.urls import path

from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('register_success/', views.SuccessRegister.as_view(), name='register_success'),
]
