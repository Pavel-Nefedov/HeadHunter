from django import forms
from django.contrib.auth.forms import UserCreationForm

from authapp.models import HHUser


class RegisterUserForm(UserCreationForm):
    USER_ROLE = [
        ('is_company', 'Работодатель'),
        ('is_candidate', 'Соискатель'),
    ]

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    user_role = forms.ChoiceField(
        label='Ваша роль',
        widget=forms.RadioSelect,
        choices=USER_ROLE,
    )
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = HHUser
        fields = (
            'username',
            'email',
            'user_role',
            'password1',
            'password2')
