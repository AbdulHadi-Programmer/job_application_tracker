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



# from django.db import models
# # New Feedback Form Page : 
# class Feedback(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     email = models.EmailField(max_length=100, default="")
#     satisfaction = models.IntegerField(choices=[
#         (1, 'Very Dissatisfied'),
#         (2, 'Dissatisfied'),
#         (3, 'Neutral'),
#         (4, 'Satisfied'),
#         (5, 'Very Satisfied')
#     ], blank=False, default=0)  # This ensures it is required (not null)

#     likes = models.TextField(default="No likes yet")
#     improvements = models.TextField(default="No value given")
#     additional_comments = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f"Feedback from {self.name if self.name else 'Anonymous'}"

from django.db import models

class Feedback(models.Model):
    # Required fields
    name = models.CharField(max_length=255)
    email = models.EmailField()
    # rating = models.PositiveSmallIntegerField()  # Values between 1-10
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 11)],  # Rating choices from 1 to 10
        default=5,  # Default value for rating field
    )
    # DISCOVERY_CHOICES = [
    #     ('social_media', 'Social Media'),
    #     ('word_of_mouth', 'Word of Mouth'),
    #     ('search_engine', 'Search Engine'),
    #     ('friend', 'Friend/Colleague'),
    #     ('advertisement', 'Advertisement'),
    #     ('other', 'Other'),
    # ]

    discovery = models.CharField(
        max_length=50,
        choices=[
            ('social_media', 'Social Media'),
            ('word_of_mouth', 'Word of Mouth'),
            ('search_engine', 'Search Engine'),
            ('friend', 'Friend/Colleague'),
            ('advertisement', 'Advertisement'),
            ('other', 'Other'),
        ],
        default='social_media',  # Add default value here
    )

    # discovery = models.CharField(max_length=50, choices=DISCOVERY_CHOICES)
    # NAVIGATION_CHOICES = [
    #     ('very_easy', 'Very Easy'),
    #     ('easy', 'Easy'),
    #     ('neutral', 'Neutral'),
    #     ('difficult', 'Difficult'),
    #     ('very_difficult', 'Very Difficult'),
    # ]
    # navigation = models.CharField(max_length=50, choices=NAVIGATION_CHOICES)
    navigation = models.CharField(
        max_length=50,
        choices=[
            ('very_easy', 'Very Easy'),
            ('easy', 'Easy'),
            ('neutral', 'Neutral'),
            ('difficult', 'Difficult'),
            ('very_difficult', 'Very Difficult'),
        ],
        default='neutral',  # Default value for navigation field
    )

    # Optional fields
    features = models.TextField(blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)
    
    # Timestamp
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.name} - Rating: {self.rating}"
