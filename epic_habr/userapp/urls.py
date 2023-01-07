
from django.urls import path
from userapp.views import login, register, profile, logout


app_name = 'userapp'

urlpatterns = [

    path('', login, name='index'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),


]

