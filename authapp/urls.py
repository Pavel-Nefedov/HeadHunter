from django.urls import path

from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login_success/', views.SuccessLogin.as_view(), name='login_success'),
    path('logout/', views.LogoutUser.as_view(), name='logout')
]
