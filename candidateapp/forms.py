from django import forms
from candidateapp.models import Candidate, ContactInfo, PositionAndSalary, WorkExperience, Education, \
    AdvancedTraining, Resume


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['user', 'first_name', 'last_name',
                  'email', 'phone_number', 'search_area']

    # def __init__(self, *args, **kwargs):
    #     super(CandidateForm, self).__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['name', 'surname', 'patronymic',
                  'birthday', 'city', 'gender', 'moving',
                  'business_trips', ]

    # def __init__(self, *args, **kwargs):
    #     super(ContactInfoForm, self).__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})


class PositionAndSalaryForm(forms.ModelForm):
    class Meta:
        model = PositionAndSalary
        fields = ['desired_position', 'salary', 'busyness',
                  'work_schedule']

    # def __init__(self, *args, **kwargs):
    #     super(PositionAndSalaryForm, self).__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['getting_started', 'end_work', 'working',
                  'organization', 'post', 'responsibilities', 'skills',
                  'about_me', ]

    # def __init__(self, *args, **kwargs):
    #     super(WorkExperienceForm, self).__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['level', 'educational_institution', 'faculty', 'specialization', 'year_graduation']

    # def __init__(self, *args, **kwargs):
    #     super(EducationForm, self).__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})


class AdvancedTrainingForm(forms.ModelForm):
    class Meta:
        model = AdvancedTraining
        fields = ['course_name', 'organization_conducted', 'specialization', 'year_graduation']

    # def __init__(self, *args, **kwargs):
    #     super(AdvancedTrainingForm, self).__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ['candidate',
                  'contact_info',
                  'position_and_salary',
                  'work_experience',
                  'education',
                  'advanced_training']

    # def __init__(self, *args, **kwargs):
    #     super(ResumeForm, self).__init__(*args, **kwargs)
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})
    # #     # for field_name, field in self.fields.items():
    # #     #     field.widget.attrs['class'] = 'form-control'
    #     self.fields['candidate'].widget.attrs['readonly'] = True
    #     self.fields['contact_info'].widget.attrs.update({'class': 'input'})


