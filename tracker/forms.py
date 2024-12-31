# forms.py
from django import forms
# from .models import Add_Job,  Feedback
from .models import *

# class JobForm(forms.ModelForm):
#     class Meta:
#         model = Add_Job
#         fields = ['job_category', 'job_level', 'company_name', 'reference_link', 'employment_type', 'application_status', 'interview_date']
#         widgets = {
#             'interview_date': forms.DateInput(attrs={'type': 'date'}),
#         }
# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ['name', 'email', 'rating', 'feedback_box']    

from django import forms
from .models import Add_Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Add_Job
        fields = ['job_category', 'job_level', 'company_name', 'company_email', 'reference_link', 'employment_type', 'application_status', 'interview_date']
        # widget=forms.Select(attrs={"class": "custom-input"})

        widgets = {
            'job_category': forms.TextInput({
                    'class': 'my-input', 
                }),
            'job_level': forms.Select(attrs={
                'class': 'my-input',
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'my-input',
            }),

            'company_email': forms.EmailInput(attrs={
                'class': 'my-input',
            }),
            'reference_link': forms.URLInput(attrs={
                'class': 'my-input',
            }),

            'employment_type': forms.Select(attrs={
                'class': 'my-input',
            }),
            'application_status': forms.Select(attrs={
                'class': 'my-input',
            }),
            'interview_date': forms.DateInput(attrs={
                'class': 'my-input',
            }),
        }

# from django import forms
# from .models import Feedback

# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ['name', 'email', 'satisfaction', 'likes', 'improvements', 'additional_comments']
