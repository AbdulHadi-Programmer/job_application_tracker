from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, User


# Create your models here.
class Add_Job(models.Model):

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
    # New With Foreign Key:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Below code is old without foreign key :
    job_category = models.CharField(max_length=100)
    job_level = models.CharField(max_length=100, choices=JOB_LEVEL_CHOICES)
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=150, null=True, blank=True)  # Company Email New Fielded Added
    reference_link = models.URLField(max_length=200)
    employment_type = models.CharField(max_length=100, choices=EMPLOYMENT_TYPE_CHOICES)
    application_status = models.CharField(max_length=20, choices=APPLICATION_STATUS_CHOICES, default='pending')  # Default status is pending
    
    # You can also add a field for the interview date
    interview_date = models.DateField(null=True, blank=True)  # Allows null values if no date is set

    def __str__(self):
        return f"{self.job_category} at {self.company_name} - Status: {self.application_status}"



class Feedback(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    rating = [
        ('5', '⭐⭐⭐⭐⭐ - Excellent'),
        ('4', '⭐⭐⭐⭐ - Good'),
        ('3', '⭐⭐⭐ - Average'),
        ('2', '⭐⭐ - Poor'),
        ('1', '⭐ - Terrible'),
    ]
    rating = models.CharField(max_length=10 ,choices=rating, default='----------')
    feedback_box = models.TextField(max_length=5000)

    def __str__(self):
        return self.name if self.name else "Anonymous Feedback"

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.core.validators import RegexValidator
# from django.contrib.auth.models import User

# # Create your models here.
# class OTP(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     otp_code = models.CharField(max_length=6)
#     created_at = models.DateTimeField(auto_now_add=True)

# class UserManager(BaseUserManager):
#     def create_user(self, username, full_name, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field is required")
#         if not username:
#             raise ValueError("The Username field is required")

#         email = self.normalize_email(email)
#         user = self.model(username=username, full_name=full_name, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, full_name, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(username, full_name, email, password, **extra_fields)


# class User(AbstractBaseUser):
#     username = models.CharField(
#         max_length=30,
#         unique=True,
#         validators=[RegexValidator(
#             regex=r'^[a-zA-Z0-9]+$',
#             message="Username must contain only letters and numbers, with no spaces or special characters."
#         )]
#     )
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     job_title = models.CharField(max_length=100, blank=True, null=True)  # Optional
#     company_name = models.CharField(max_length=100, blank=True, null=True)  # Optional
#     country = models.CharField(max_length=50)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['full_name', 'email', 'country']

#     def __str__(self):
#         return self.username

