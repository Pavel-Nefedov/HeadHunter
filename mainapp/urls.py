from django.urls import path

from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('portal_rules/', views.PortalRules.as_view(), name='portal_rules'),
]
