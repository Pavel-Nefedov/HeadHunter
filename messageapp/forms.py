from django.forms import ModelForm, TextInput

from messageapp.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}
        widgets = {
            'message': TextInput(attrs={
                'class': "form-control",
                'style': 'padding-bottom : 10px',
                'placeholder': 'Введите сообщение'
                }),
        }
