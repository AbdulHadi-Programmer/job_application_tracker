# forms.py
from django import forms
from .models import Add_Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Add_Job
        fields = ['job_category', 'job_level', 'company_name', 'reference_link', 'employment_type', 'application_status', 'interview_date']
        widgets = {
            'interview_date': forms.DateInput(attrs={'type': 'date'}),
        }