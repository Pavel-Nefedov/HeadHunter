from django.urls import path

from messageapp.views import DialogsView, MessagesView, CreateDialogView, ModeratorApproveView, ModeratorRejectView, \
    ResponseToVacancyView, ResponseToResumeView

app_name = 'messageapp'

urlpatterns = [

    path('', DialogsView.as_view(), name='dialogs'),
    path('create/<user_id>/', CreateDialogView.as_view(), name='create_dialog'),
    path('<chat_id>/', MessagesView.as_view(), name='messages'),
    path(
        'approve_after_moderation/<int:user_id>/<int:query_set_id>/<str:approve_type>',
        ModeratorApproveView.as_view(),
        name='approve_after_moderation'
    ),
    path(
        'reject_after_moderation/<int:user_id>/<int:query_set_id>/<str:reject_type>',
        ModeratorRejectView.as_view(),
        name='reject_after_moderation'
    ),
    path(
        'response_to_vacancy/<int:user_id>/<int:vacancy_id>',
        ResponseToVacancyView.as_view(),
        name='response_to_vacancy'
    ),
    path(
        'response_to_resume/<int:user_id>/<int:resume_id>',
        ResponseToResumeView.as_view(),
        name='response_to_resume'
    ),
]
