from django.urls import path

from moderatorapp.views import ModeratorLkIndex

app_name = 'moderatorapp'

urlpatterns = [
    path('lk/', ModeratorLkIndex.as_view(), name='moderator_lk'),
]
