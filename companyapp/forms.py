from django import forms
from django.contrib.auth.forms import UserChangeForm
from models import CompanyProfile


class CompanyProfileForm(UserChangeForm):
    company_logo = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = CompanyProfile
        fields = ('user', 'company_logo', 'company_name', 'legal_entity', 'company_address','company_address','email','phone_number', 'about_company')

    def __init__(self, *args, **kwargs):
        super(CompanyProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['user'].widget.attrs['readonly'] = True
        self.fields['company_logo'].widget.attrs['class'] = 'custom-file-input'

