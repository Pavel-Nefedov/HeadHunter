from django.urls import path

from moderatorapp.views import ModeratorLkIndex, ModeratorLkResume, ModeratorLkCompanyProfile, ModeratorLkVacancy

app_name = 'moderatorapp'

urlpatterns = [
    path('lk/', ModeratorLkIndex.as_view(), name='moderator_lk'),
    path('lk/resume', ModeratorLkResume.as_view(), name='moderator_lk_resume'),
    path('lk/company_profile', ModeratorLkCompanyProfile.as_view(), name='moderator_lk_company_profile'),
    path('lk/vacancy', ModeratorLkVacancy.as_view(), name='moderator_lk_vacancy'),
]
