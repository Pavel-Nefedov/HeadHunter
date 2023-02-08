from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('mainapp.urls', namespace='mainapp')),
                  path('auth/', include('authapp.urls', namespace='authapp')),
                  path('candidate/', include('candidateapp.urls', namespace='candidate')),
                  path('company/', include('companyapp.urls', namespace='company')),
                  path('dialogs/', include('messageapp.urls', namespace='message')),
                  path('moderator/', include('moderatorapp.urls', namespace='moderator')),
                  path("favorites/", include("favoriteapp.urls", namespace="favorite")),
              ]

if settings.DEBUG:
    import debug_toolbar

    # Подключим дебагпанель
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
