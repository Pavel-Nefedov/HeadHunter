from django import forms

from candidateapp.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'moving',
            'business_trips',
            'desired_position',
            'salary',
            'busyness',
            'work_schedule',
            'getting_started',
            'end_work',
            'working',
            'organization',
            'post',
            'responsibilities',
            'skills',
            'about_me',
            'level',
            'educational_institution',
            'faculty',
            'specialization',
            'year_graduation',
            'course_name',
            'organization_conducted',
            'specialization_course',
            'year_graduation_course',
            'is_draft'
        ]

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input'

