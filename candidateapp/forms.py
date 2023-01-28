# from django import forms
# from django.contrib.auth.forms import UserCreationForm
#
# from candidate.models import Candidate
#
#
# class RegisterCandidateForm(UserCreationForm):
#     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     patronymic = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
#     phone_number = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     search_area = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-input'}))
#
#     class Meta:
#         model = Candidate
#         fields = (
#             'username',
#             'email',
#             'phone_number',
#             'search_area')
