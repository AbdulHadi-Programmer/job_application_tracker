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
