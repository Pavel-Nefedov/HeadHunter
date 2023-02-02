"""agile_hh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

# from companyapp.views import VacancySearch, VacancyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='mainapp')),
    path('auth/', include('authapp.urls', namespace='authapp')),
    path('candidate/', include('candidateapp.urls', namespace='candidate')),
    path('company/', include('companyapp.urls', namespace='company')),
    path('dialogs/', include('messageapp.urls', namespace='message')),
    path('moderator/', include('moderatorapp.urls', namespace='moderator')),
]

if settings.DEBUG:
    import debug_toolbar

    # Подключим дебагпанель
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
