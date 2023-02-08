from django import forms

from companyapp.models import CompanyProfile, Vacancy


class CompanyProfileForm(forms.ModelForm):
    # company_logo = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = CompanyProfile
        fields = (
            'company_logo',
            'company_name',
            'legal_entity',
            'company_address',
            'company_address',
            'email',
            'phone_number',
            'about_company'
        )

    def __init__(self, *args, **kwargs):
        super(CompanyProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input'
        self.fields['company_logo'].widget.attrs['class'] = 'form-input'
        self.fields['company_logo'].required = False


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = (
            'vacancy_name',
            'city',
            'duties_description',
            'requirements_description',
            'work_conditions',
            'salary_min',
            'salary_max',
            'currency',
            'is_for_disabled',
            'is_full_day',
            'is_intern',
        )
