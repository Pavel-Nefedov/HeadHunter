from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [

    path('', mainapp.main, name='index'),
    path('<uuid:uid>/', mainapp.get_article, name='article'),
    path('delete/<uuid:uid>/', mainapp.delete_article, name='delete'),
    path('<str:subject>/', mainapp.get_subject_related_articles, name='subject_related_articles'),
    path('hub/<str:hub_en_name>/', mainapp.get_hub_related_articles, name='hub_related_articles'),

]
