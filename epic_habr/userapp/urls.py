from django.urls import path
import mainapp.views as mainapp
from userapp.views import login, register

app_name = 'userapp'

urlpatterns = [

    path('', login, name='index'),
    path('register/', register, name='register'),


]
