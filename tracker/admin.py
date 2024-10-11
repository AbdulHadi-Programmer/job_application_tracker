from django.contrib import admin
from .models import Add_Job

class AddJobAdmin(admin.ModelAdmin):
    list_display = ('job_category', 'job_level', 'company_name', 'employment_type')  # Fields to display in the list view
    search_fields = ('company_name', 'job_category')  # Fields to search
    list_filter = ('job_level', 'employment_type')  # Filters for the list view

admin.site.register(Add_Job, AddJobAdmin)

# Simply add:
# admin.site.register(Add_Job)
