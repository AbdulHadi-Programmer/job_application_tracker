from django.db import models
from django.contrib.auth.models import BaseUserManager, User
from django.utils.translation import gettext_lazy as _

# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError(_("The Email field must be set"))
#         if not username:
#             raise ValueError(_("The Username field must be set"))
        
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)  # Hash the password
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(username, email, password, **extra_fields)

# class User(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=150)

#     objects = UserManager()  # Use the custom manager

#     def __str__(self):
#         return self.username

#     def set_password(self, password):
#         """Hash the password using Django's built-in password hashing."""
#         from django.contrib.auth.hashers import make_password
#         self.password = make_password(password)



# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# class UserAdmin(BaseUserAdmin):
#     list_display = ('email', 'username', 'is_staff', 'is_active')
#     list_filter = ('is_staff', 'is_active')
#     search_fields = ('email', 'username')
#     ordering = ('email',)
# admin.site.register(User, UserAdmin)

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError(_("The Email field must be set"))
#         if not username:
#             raise ValueError(_("The Username field must be set"))
        
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)  # Hash the password
#         user.save(using=self._db)
#         return user

    # def create_superuser(self, username, email, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)

    #     return self.create_user(username, email, password, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     groups = models.ManyToManyField(Group, blank=True)
#     user_permissions = models.ManyToManyField(Permission, blank=True)

#     objects = UserManager()  # Use the custom manager

#     REQUIRED_FIELDS = []  # No additional fields are required
#     USERNAME_FIELD = 'username'  # The field to use when authenticating

#     def __str__(self):
# #         return self.username


# #########################################################################################################
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# class UserAdmin(BaseUserAdmin):
#     list_display = ('email', 'username', 'is_staff', 'is_active')
#     list_filter = ('is_staff', 'is_active')
#     search_fields = ('email', 'username')
#     ordering = ('email',)

# admin.site.register(User, UserAdmin)
##########################################################################################################

# Create your models here.
class Add_Job(models.Model):
    # Add this ForeignKey to link jobs to specific users
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    # The above is giving me more and more error: 

    JOB_LEVEL_CHOICES = [
        ('intern', 'Intern'),
        ('junior', 'Junior'),
        ('mid', 'Mid-Level'),
        ('senior', 'Senior'),
        ('lead', 'Lead'),
        ('manager', 'Manager'),
        ('director', 'Director'),
        ('vp', 'Vice President'),
        ('c_level', 'C-Level'),
    ]

    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'Full-Time'),
        ('part_time', 'Part-Time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
        ('apprenticeship', 'Apprenticeship'),
    ]

    APPLICATION_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('applied', 'Applied'),
        ('interview', 'Interview Scheduled'),
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
        ('offer_accepted', 'Offer Accepted'),
        ('offer_declined', 'Offer Declined'),
    ]

    job_category = models.CharField(max_length=100)
    job_level = models.CharField(max_length=100, choices=JOB_LEVEL_CHOICES)
    company_name = models.CharField(max_length=100)
    reference_link = models.URLField(max_length=200)
    employment_type = models.CharField(max_length=100, choices=EMPLOYMENT_TYPE_CHOICES)
    application_status = models.CharField(max_length=20, choices=APPLICATION_STATUS_CHOICES, default='pending')  # Default status is pending
    
    # You can also add a field for the interview date
    interview_date = models.DateField(null=True, blank=True)  # Allows null values if no date is set

    def __str__(self):
        return f"{self.job_category} at {self.company_name} - Status: {self.application_status}"


class Add_Email_Template(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=5000)

