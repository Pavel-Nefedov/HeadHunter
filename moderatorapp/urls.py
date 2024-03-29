from django.urls import path

from moderatorapp.views import ModeratorLkIndex, ModeratorLkResume, ModeratorLkCompanyProfile, ModeratorLkVacancy, \
    ModeratorLkResumeModerate, ModeratorLkCompanyProfileModerate, ModeratorLkVacancyModerate

app_name = 'moderatorapp'

urlpatterns = [
    path('lk/', ModeratorLkIndex.as_view(), name='moderator_lk'),
    path('lk/resume', ModeratorLkResume.as_view(), name='moderator_lk_resume'),
    path('lk/company_profile', ModeratorLkCompanyProfile.as_view(), name='moderator_lk_company_profile'),
    path('lk/vacancy', ModeratorLkVacancy.as_view(), name='moderator_lk_vacancy'),
    path('lk/resume/moderate/<int:pk>', ModeratorLkResumeModerate.as_view(), name='moderator_lk_resume_moderate'),
    path(
        'lk/company_profile/moderate/<int:pk>',
        ModeratorLkCompanyProfileModerate.as_view(),
        name='moderator_lk_company_profile_moderate'
    ),
    path(
        'lk/vacancy/moderate/<int:pk>',
        ModeratorLkVacancyModerate.as_view(),
        name='moderator_lk_vacancy_moderate'
    ),

]
