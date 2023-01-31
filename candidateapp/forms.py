from django import forms
from candidateapp.models import Resume


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('candidate', 'contact_info', 'position_and_salary',
                  'work_experience', 'education', 'advanced_training')


