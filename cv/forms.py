from django import forms
from cv.models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'project_description', 'github_link')


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('start_date', 'end_date', 'company', 'description')


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ('name', 'date_of_birth', 'email_address')


class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ('institution', 'grades')
