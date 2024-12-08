from django.contrib import admin
from authentication.models import OTP
from .models import UserProfile

# Register your models here.
admin.site.register(OTP)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'country')  # Fields to display in the admin panel
