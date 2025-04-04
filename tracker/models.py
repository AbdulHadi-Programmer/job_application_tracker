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
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 11)],  # Rating choices from 1 to 10
        default=5,  # Default value for rating field
    )
    

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


# class Profile(models.Model):
#     # personal detail 
#     image = models.ImageField(upload_to="", null=True)
#     name = models.CharField(max_length=50)
#     short_address = models.CharField(max_length=60)  # city and country 
#     # Online Profile:
#     # All social media include : github, linkedin, fb, insta, twitter, stackoverflow, etc
#     # Add a dynamic fields so the user can add as much as he want 
#     # Contact Information : 
#     full_name = models.CharField(max_length=200, null=True, blank=True)
#     email = models.EmailField(max_length=100)
#     phone = models.CharField(max_length=15)
#     address = models.CharField(max_length=200)
#     # Skills:
# #     Python      90%
# #     Django      70%
# #     HTML & CSS  50%
#     # Also as i am confused for writing a skill fields as it is shown in progress bar form so that why each skill has percentage to show so how to store both of them and also how to take input
#     skill1 = models.CharField(max_length=120, null=True, blank=True)
#     percentage1 = models.PositiveIntegerField()
#     # Add a dynamic field to add more field as skills 
#     skill2 = models.CharField(max_length=120, null=True, blank=True)
#     percentage2 = models.PositiveIntegerField()
#     skill3 = models.CharField(max_length=120, null=True, blank=True)
#     percentage3 = models.PositiveIntegerField()
#     skill4 = models.CharField(max_length=120, null=True, blank=True)
#     percentage4 = models.PositiveIntegerField()
#     skill5 = models.CharField(max_length=120, null=True, blank=True)
#     percentage5 = models.PositiveIntegerField()
#     # Projects with Status :
#     # In this projects added, maximum 5 and minimum zero, status should be 'completed', 'in progress' and 'pending'
#     # also each project must be associated with the status

############################################################################################################################################################################################################################################################################################################################################################
# from django.core.exceptions import ValidationError
# from django.db import models

# class UserProfile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="user_images/", blank=True, null=True)
#     full_name = models.CharField(max_length=100, blank=True, null=True)
#     job_title = models.CharField(max_length=120, blank=True, null=True)
#     region = models.CharField(max_length=150, blank=True, null=True)

#     # Contact Information
#     email = models.EmailField(blank=True, null=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     location = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.user.username  # Display the username instead of "UserProfile object (1)"
   
   

# class SocialProfile(models.Model):
#     profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='social_profiles')
#     platform_name = models.CharField(max_length=255)
#     profile_link = models.URLField()

#     def clean(self):
#         # if SocialProfile.objects.filter(user=self.user).count() >= 3:
#         if SocialProfile.objects.filter(profile=self.profile).count() >= 3:
#             raise ValidationError("You can only have up to 3 social profiles.")

#     def save(self, *args, **kwargs):
#         self.clean()
#         super().save(*args, **kwargs)


# class Skill(models.Model):
#     profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     proficiency = models.IntegerField()

#     def clean(self):
#         if Skill.objects.filter(profile=self.profile).count() >= 3:
#             raise ValidationError("You can only have up to 3 skills.")

#     def save(self, *args, **kwargs):
#         self.clean()  # Ensure validation runs before saving
#         super().save(*args, **kwargs)



# class Project(models.Model):
#     profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="projects")
#     project_name = models.CharField(max_length=200)
#     project_status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')])

#     def __str__(self):
#         return f"{self.project_name} - {self.project_status}"
    
#     def save(self, *args, **kwargs):
#         if self.profile.projects.count() >= 3:
#             raise ValidationError('You can add up to 3 projects.')
#         super().save(*args, **kwargs)
############################################################################################################################################################################################################################################################################

# from django.core.exceptions import ValidationError
# from django.db import models
# from django.contrib.auth.models import User  # Ensure User is imported

# class UserProfile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensure one profile per user
#     # user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="user_images/", blank=True, null=True)
#     full_name = models.CharField(max_length=100, blank=True, null=True)
#     job_title = models.CharField(max_length=120, blank=True, null=True)
#     region = models.CharField(max_length=150, blank=True, null=True)

#     # Contact Information   
#     email = models.EmailField(blank=True, null=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     location = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.user.username  # Display the username instead of "UserProfile object (1)"

# class SocialProfile(models.Model):
#     profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_profiles')
#     platform_name = models.CharField(max_length=255)
#     profile_link = models.URLField()

#     def clean(self):
#         if not self.profile_id:  # Ensure profile is set before checking constraints
#             return
        
#         if SocialProfile.objects.filter(profile=self.profile).count() >= 3:
#             raise ValidationError("You can only have up to 3 social profiles.")

#     def save(self, *args, **kwargs):
#         if not self.profile_id:
#             raise ValidationError("Profile must be set before saving a social profile.")
        
#         self.clean()
#         super().save(*args, **kwargs)


# class Skill(models.Model):
#     profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills")  # Change `user` to `profile`
#     skill_name = models.CharField(max_length=100)
#     proficiency = models.IntegerField()

#     def clean(self):
#         if Skill.objects.filter(profile=self.profile).count() >= 3:  # Change `user` to `profile`
#             raise ValidationError("You can only have up to 3 skills.")

#     def save(self, *args, **kwargs):
#         self.clean()  # Ensure validation runs before saving
#         super().save(*args, **kwargs)

# class Project(models.Model):
#     profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
#     project_name = models.CharField(max_length=200)
#     project_status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')])

#     def __str__(self):
#         return f"{self.project_name} - {self.project_status}"

#     def save(self, *args, **kwargs):
#         if self.profile.projects.count() >= 3:
#             raise ValidationError('You can add up to 3 projects.')
#         super().save(*args, **kwargs)
#################################################################################################################################################################################################################################################################################

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.full_name


class SocialProfile(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='social_profiles')
    platform_name = models.CharField(max_length=100)
    profile_link = models.URLField()

    def __str__(self):
        return f"{self.platform_name} - {self.user_profile.full_name}"


class Skill(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=100)
    # proficiency = models.CharField(max_length=50, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
    proficiency = models.IntegerField()

    def __str__(self):
        return f"{self.skill_name} - {self.user_profile.full_name}"



class Project(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=100)
    project_status = models.CharField(max_length=50, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')])

    def __str__(self):
        return f"{self.project_name} - {self.user_profile.full_name}"


