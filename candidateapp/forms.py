from django import forms
from candidateapp.models import Resume



class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ['candidate', 'name', 'surname', 'patronymic',
                  'birthday', 'city', 'gender', 'moving',
                  'business_trips', 'desired_position', 'salary', 'busyness',
                  'work_schedule', 'getting_started', 'end_work', 'working',
                  'organization', 'post', 'responsibilities', 'skills',
                  'about_me', 'level', 'educational_institution', 'faculty', 'specialization', 'year_graduation',
                  'course_name', 'organization_conducted', 'specialization_course', 'year_graduation_course']



