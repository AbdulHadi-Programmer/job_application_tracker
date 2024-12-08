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
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'feedback_box']    

class JobForm(forms.ModelForm):
    class Meta:
        model = Add_Job
        fields = ['job_category', 'job_level', 'company_name', 'company_email', 'reference_link', 'employment_type', 'application_status', 'interview_date']
        widgets = {
            'job_category': forms.TextInput(attrs={
                'style': 'padding: 8px !important; width: calc(100% - 20px); box-sizing: border-box; margin-right: 30px; border: 1px solid #ddd; border-radius: 5px; font-size: 15px;',
                'required': True,
            }),
            'job_level': forms.Select(attrs={
                'style': 'padding: 8px !important; width: calc(100% - 20px); box-sizing: border-box; margin-right: 30px; border: 1px solid #ddd; border-radius: 5px; font-size: 15px;',
                'required': True,
            }),
            'company_name': forms.TextInput(attrs={
                'style': 'padding: 8px !important; width: calc(100% - 20px); box-sizing: border-box; margin-right: 30px; border: 1px solid #ddd; border-radius: 5px; font-size: 15px;',
                'required': True,
            }),
            'company_email': forms.EmailInput(attrs={
                'style': 'padding: 8px; width: calc(100% - 20px); box-sizing: border-box; margin-right: 30px; border: 1px solid #ddd; border-radius: 5px; font-size: 15px;',
                # 'required': True,
            }),
            'reference_link': forms.URLInput(attrs={
                'style': 'padding: 8px !important; width: calc(100% - 20px); box-sizing: border-box; margin-right: 30px; border: 1px solid #ddd; border-radius: 5px; font-size: 15px;',
                'required': True,
            }),
            'employment_type': forms.Select(attrs={
                'style': 'padding: 8px !important; width: calc(100% - 20px); box-sizing: border-box; margin-right: 30px; border: 1px solid #ddd; border-radius: 5px; font-size: 15px;',
                'required': True,
            }),
            'application_status': forms.Select(attrs={
                'style': 'padding: 8px !important; width: calc(100% - 20px); box-sizing: border-box; margin-right: 30px; border: 1px solid #ddd; border-radius: 5px; font-size: 15px;',
                'required': True,
            }),
            'interview_date': forms.DateInput(attrs={
                'type': 'date',
                'style': 'padding: 8px !important; width: calc(100% - 20px); box-sizing: border-box; margin-right: 30px; border: 1px solid #ddd; border-radius: 5px; font-size: 15px;',
            }),
        }

# from django import forms
# from django.contrib.auth.models import User
# from django.core.validators import RegexValidator
# from django.core.exceptions import ValidationError

# class SignupForm(forms.ModelForm):
#     full_name = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput)         # Password 
#     confirm_password = forms.CharField(widget=forms.PasswordInput) # Confirm Password
#     job_title = forms.CharField(max_length=100, required=False)    # Job title (Optional)
#     company_name = forms.CharField(max_length=100, required=False)  # Company (Optional)
#     country = forms.CharField(max_length=50, required=True)         # Country (Required)
#     username = forms.CharField(
#         max_length=30,
#         required=True,
#         validators=[RegexValidator(
#             regex=r'^[a-zA-Z0-9]+$',
#             message="Username must contain only letters and numbers, with no spaces or special characters."
#         )]
#     )

#     class Meta:
#         model = User
#         fields = ['username', 'full_name', 'email', 'password', 'confirm_password', 'job_title', 'company_name', 'country']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             raise ValidationError("Passwords do not match.")

        