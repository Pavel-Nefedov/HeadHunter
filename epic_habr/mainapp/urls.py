from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [

    path('', mainapp.main, name='index'),
    path('<int:pk>/', mainapp.get_article, name='article'),
    path('<str:subject>/', mainapp.get_subject_related_articles, name='subject_related_articles'),

]
