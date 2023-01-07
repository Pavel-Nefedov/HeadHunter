from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from userapp.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'username_class', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password_class', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs['class']:
                field.widget.attrs['class'] += ' class_for_all_fields'
            else:
                field.widget.attrs['class'] = 'class_for_all_fields'


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'first_name_class', 'placeholder': 'Введите Ваше имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'last_name_class', 'placeholder': 'Введите Вашу фамилию'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'username_class', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'email_class', 'placeholder': 'Введите Вашу почту'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password_class', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password_class', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs['class']:
                field.widget.attrs['class'] += ' class_for_all_fields'
            else:
                field.widget.attrs['class'] = 'class_for_all_fields'


class UserProfileForm(UserChangeForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'username_class readonly', 'readonly': True}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'email_class readonly', 'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput())

    # first_name = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'first_name_class', 'placeholder': 'Введите Ваше имя'}))
    # last_name = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'last_name_class', 'placeholder': 'Введите Вашу фамилию'}))
    #
    # email = forms.CharField(
    #     widget=forms.EmailInput(attrs={'class': 'email_class', 'placeholder': 'Введите Вашу почту'}))
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class': 'password_class', 'placeholder': 'Введите пароль'}))
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class': 'password_class', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' class_for_all_fields'
            else:
                field.widget.attrs['class'] = 'class_for_all_fields'
            self.fields['image'].widget.attrs['class'] = 'custom-file-input'