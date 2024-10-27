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


class Add_Email_Template(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(max_length=5000)

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

