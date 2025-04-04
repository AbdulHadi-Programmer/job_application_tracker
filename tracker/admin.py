from django.contrib import admin
from .models import Add_Job, Feedback

class AddJobAdmin(admin.ModelAdmin):
    list_display = ('job_category', 'job_level', 'company_name', 'employment_type', 'user')  # Fields to display in the list view
    search_fields = ('company_name', 'job_category')  # Fields to search
    list_filter = ('job_level', 'employment_type', 'user')  # Filters for the list view, added 'user'

admin.site.register(Add_Job, AddJobAdmin)

from django.contrib import admin
from .models import Feedback

# class FeedbackAdmin1(admin.ModelAdmin):
#     list_display = ('name', 'email', 'satisfaction', 'likes', 'improvements', 'additional_comments')

# admin.site.register(Feedback, FeedbackAdmin1)
admin.site.register(Feedback)

# =====================================================================================================================

# from django.contrib import admin
# from .models import UserProfile, Project

# # Register the UserProfile model
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('image', 'full_name', 'job_title', 'region', 'email', 'phone', 'location')
#     search_fields = ('full_name', 'email')

# admin.site.register(UserProfile, UserProfileAdmin)

# from django.contrib import admin
# from .models import Project, SocialProfile, Skill

# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('project_name', 'profile', 'project_status')  # Fields to display in the list view
#     list_filter = ('project_status', 'profile')  # Add filter options
#     search_fields = ('project_name',)  # Fields to search by
#     ordering = ('profile',)  # Optional: Define the default ordering

#     def save_model(self, request, obj, form, change):
#         if obj.profile.projects.count() >= 3:
#             raise ValueError('You can add up to 3 projects.')
#         super().save_model(request, obj, form, change)

# # Register the Project model with the custom admin class
# admin.site.register(Project, ProjectAdmin)


# class SocialProfileAdmin(admin.ModelAdmin):
#     list_display = ('profile', 'platform_name', 'profile_link')
#     list_filter = ('profile', 'platform_name', 'profile_link')

#     def save_model(self, request, obj, form, change):
#         if obj.profile.social_profiles.count() >= 3:
#             raise ValueError('You can add up to 3 platforms.')
#         super().save_model(request, obj, form, change)

# admin.site.register(SocialProfile, SocialProfileAdmin)


# class SkillAdmin(admin.ModelAdmin):
#     list_display = ( 'profile', 'skill_name', 'proficiency')
#     list_filter = ( 'profile', 'skill_name', 'proficiency')
    
# admin.site.register(Skill, SkillAdmin)

# from django.contrib import admin
# from .models import UserProfile, SocialProfile, Skill, Project

# class SocialProfileInline(admin.TabularInline):
#     model = SocialProfile
#     extra = 0  # Prevent unnecessary empty forms
#     max_num = 3  # Limit to 3

# class SkillInline(admin.TabularInline):
#     model = Skill
#     extra = 0
#     max_num = 3

# class ProjectInline(admin.TabularInline):
#     model = Project
#     extra = 0
#     max_num = 3

# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'full_name', 'job_title', 'email', 'phone']
#     inlines = [SocialProfileInline, SkillInline, ProjectInline]  # Inline related models

# @admin.register(SocialProfile)
# class SocialProfileAdmin(admin.ModelAdmin):
#     list_display = ['profile', 'platform_name', 'profile_link']

# @admin.register(Skill)
# class SkillAdmin(admin.ModelAdmin):
#     list_display = ['profile', 'skill_name', 'proficiency']

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ['profile', 'project_name', 'project_status']



from django.contrib import admin
from .models import UserProfile, SocialProfile, Skill, Project

class SocialProfileInline(admin.TabularInline):
    model = SocialProfile
    extra = 0  
    max_num = 3  

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0
    max_num = 3

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 0
    max_num = 3

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'job_title', 'region', 'email', 'phone', 'location', 'image']
    list_filter = ['user', 'full_name', 'job_title'] 
    inlines = [SocialProfileInline, SkillInline, ProjectInline]

@admin.register(SocialProfile)
class SocialProfileAdmin(admin.ModelAdmin):
    list_filter = ['user_profile', 'platform_name']
    list_display = ['user_profile', 'platform_name', 'profile_link']  # Fixed

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_filter = ['user_profile', 'skill_name']
    list_display = ['user_profile', 'skill_name', 'proficiency']  # Fixed

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ['user_profile']
    list_display = ['user_profile', 'project_name', 'project_status']  # Fixed
