# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.
# class OTP(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     otp_code = models.CharField(max_length=6)
#     created_at = models.DateTimeField(auto_now_add=True)

# ## User Profile is created because to store all other optional fields
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     job_title = models.CharField(max_length=255, blank=True, null=True)
#     country = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.user.username

## The above has issued in view not in above model but i can comment it : 
# ==================================================================================================================
# ==================================================================================================================
# ==================================================================================================================

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

# # Other my code to add more fields in my projects: 
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     job_title = models.CharField(max_length=255, blank=True, null=True)
#     country = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.user.username

