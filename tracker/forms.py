# forms.py
from django import forms
# from .models import Add_Job,  Feedback
from .models import *


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



from django import forms
from .models import UserProfile, SocialProfile, Skill, Project

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'full_name', 'job_title', 'region', 'email', 'phone', 'location']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'image'}),
            'full_name': forms.TextInput(attrs={'class': 'full_name'}),
            'job_title': forms.TextInput(attrs={'class': 'job_title'}),
            'region': forms.TextInput(attrs={'class': 'region'}),
            'email': forms.EmailInput(attrs={'class': 'email', 'type': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'phone'}),  # Changed from NumberInput to TextInput
            'location': forms.TextInput(attrs={'class': 'location'}),
        }


class SocialProfileForm(forms.ModelForm):
    class Meta:
        model = SocialProfile
        fields = ['platform_name', 'profile_link']
        widgets = {
            'platform_name': forms.TextInput(attrs={'class': 'platform_name'}),
            'profile_link': forms.URLInput(attrs={'class': 'profile_link'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        user_profile = self.instance.user_profile  # Get the user profile
        # Count skills excluding the current instance (if updating)
        existing_profiles = SocialProfile.objects.filter(user_profile=user_profile).exclude(id=self.instance.id).count()
        if existing_profiles >= 3:
            raise forms.ValidationError("You can only have up to 3 Social Profile.")
        return cleaned_data


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name', 'proficiency']
        widgets = {
            'skill_name': forms.TextInput(attrs={'class': 'skill_name'}),
            'proficiency': forms.NumberInput(attrs={'class': 'proficiency'}), 
        }

    def clean(self):
        cleaned_data = super().clean()
        user_profile = self.instance.user_profile  # Get the user profile

        # Count skills excluding the current instance (if updating)
        existing_skills = Skill.objects.filter(user_profile=user_profile).exclude(id=self.instance.id).count()

        if existing_skills >= 3:
            raise forms.ValidationError("You can only have up to 3 skills.")
        
        return cleaned_data


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_status']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'project_name'}),
            'project_status': forms.Select(attrs={'class': 'project_status'})
        }

    def clean(self):
        cleaned_data = super().clean()
        user_profile = self.instance.user_profile  # Get user profile

        # 🛠️ Exclude the current project if editing, count only other projects
        existing_projects = Project.objects.filter(user_profile=user_profile).exclude(pk=self.instance.pk).count()

        if existing_projects >= 3:
            raise forms.ValidationError("You can only have up to 3 projects.")  
        
        return cleaned_data  # ✅ Ensure cleaned data is returned.
    