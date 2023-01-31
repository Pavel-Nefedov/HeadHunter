from django.urls import path

from messageapp.views import DialogsView, MessagesView, CreateDialogView

app_name = 'messageapp'

urlpatterns = [

    path('', DialogsView.as_view(), name='dialogs'),
    path('create/<user_id>/', CreateDialogView.as_view(), name='create_dialog'),
    path('<chat_id>/', MessagesView.as_view(), name='messages'),
]
