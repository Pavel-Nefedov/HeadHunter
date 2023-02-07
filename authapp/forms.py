from django import forms
from django.contrib.auth.forms import UserCreationForm

from authapp.models import HHUser, GenderChoices


class RegisterUserForm(UserCreationForm):
    USER_ROLE = [
        ('is_company', 'Работодатель'),
        ('is_candidate', 'Соискатель'),
    ]
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    patronymic = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-input'}))

    birthday = forms.CharField(label='Дата рождения', widget=forms.TextInput(attrs={'class': 'form-input'}))
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'form-input'}))
    gender = forms.ChoiceField(
        label='Пол',
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=GenderChoices.choices
    )

    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    user_role = forms.ChoiceField(
        label='Ваша роль',
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=USER_ROLE
    )
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = HHUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'patronymic',
            'email',
            'user_role',
            'password1',
            'password2')
