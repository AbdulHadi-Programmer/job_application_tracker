# This is a function to search a job 
# views.py
import json
# from .forms import FeedbackForm
from .models import Feedback 
from django.db.models import Count  # Ensure Count is imported
from django.utils import timezone  # Ensure timezone is imported
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from .forms import  *
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Specific Home page to display without logout : 
def home_page_default(request):
    return render(request, 'home_page.html')


def home_page(request):
    """
    If the user is authenticated, redirect to the job list.
    Otherwise, render the home page.
    """
    if request.user.is_authenticated:
        return redirect('job_list')  # Authenticated users are redirected
    return render(request, 'home_page.html')    # Unauthenticated users see the homepage


@login_required
def job_list(request):
    # Filter jobs by the logged-in user
    jobs = Add_Job.objects.filter(user=request.user).order_by("-interview_date")
    
    # Capture search query (if available)
    job_category = request.GET.get('job_category')

    # Apply search filter if a category is provided
    if job_category:
        jobs = jobs.filter(job_category__icontains=job_category)  # Use 'icontains' for partial match

    # Check if all company_email fields are empty or None
    all_emails_empty = not any(job.company_email for job in jobs)
    all_dates_empty = not any(job.interview_date for job in jobs)

    context = {
        'jobs': jobs,
        'all_emails_empty': all_emails_empty,  # Pass the flag to the template
        'all_dates_empty': all_dates_empty,
    }
    return render(request, 'job_list.html', context)




# @login_required # (with Foreign Key new code)
# def job_create(request):
#     if request.method == 'POST':
#         form = JobForm(request.POST)
#         if form.is_valid():
#             job = form.save(commit=False)
#             job.user = request.user  # Automatically assign the current user
#             job.save()
#             messages.success(request, 'Job created successfully!')
#             return redirect('job_list')
#     else:
#         form = JobForm()
#     return render(request, 'job_form.html', {'form': form})


# @login_required # (with Foreign Key new code)
# def job_update(request, job_id):
#     job = get_object_or_404(Add_Job, id=job_id, user=request.user)  # Ensure the job belongs to the current user
#     if request.method == 'POST':
#         form = JobForm(request.POST, instance=job)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Job updated successfully!')
#             return redirect('job_list')
#     else:
#         form = JobForm(instance=job)
#     return render(request, 'job_update.html', {'form': form, 'job': job})

@login_required
def job_create_or_update(request, job_id=None):
    if job_id:
        # Edit existing job
        job = get_object_or_404(Add_Job, id=job_id, user=request.user)
        form = JobForm(request.POST or None, instance=job)
        action = 'Update'
    else:
        # Create new job
        job = None
        form = JobForm(request.POST or None)
        action = 'Add'
    
    if request.method == 'POST':
        if form.is_valid():
            job_instance = form.save(commit=False)
            job_instance.user = request.user  # Automatically assign the current user
            job_instance.save()
            messages.success(request, f'Job {action.lower()}d successfully!')
            return redirect('job_list')
    
    return render(request, 'job_form.html', {'form': form, 'job': job, 'action': action})


@login_required
def job_delete(request, id):
    job = get_object_or_404(Add_Job, id=id, user=request.user)  # Ensure the job belongs to the current user
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('job_list')
    
    return render(request, 'job_list.html', {'job': job})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Add_Job

@login_required
def job_delete_confirmation(request, id):
    job = get_object_or_404(Add_Job, id=id, user=request.user)  # Ensure the job belongs to the current user
    
    if request.method == 'POST':
        # If POST request, delete the job and redirect
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('job_list')
    
    # If GET request, render confirmation page
    return render(request, 'job_delete_confirmation.html', {'job': job})


def logout_view(request):
    logout(request)             
    return redirect('login')  




######################################################################################################################################

def search(request):
    try:
        # Filter job listings by the logged-in user
        data = Add_Job.objects.filter(user=request.user)

        if request.method == 'GET':
            job_category = request.GET.get('job_category', '').strip()

            if job_category:
                # data = data.filter(Add_Job(job_category__icontains=job_category))  # Partial match
                data = data.filter(job_category__icontains=job_category)

        context = {
            'data': data,
        }

        return render(request, 'job_list.html', context)

    except Add_Job.DoesNotExist:
        context = {
            'error_message': 'No jobs found matching your criteria.',
            'data': []
        }
        return render(request, 'job_list.html', context)

    except Exception as e:
        context = {
            'error_message': f"An unexpected error occurred: {str(e)}",
            'data': []
        }
        return render(request, 'job_list.html', context)

###########################################################################################################

def profile(request):
    return render(request, "profile.html") 


from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib.auth.decorators import login_required

@login_required
def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        rating = request.POST.get("rating")
        discovery = request.POST.get("discovery")
        features = request.POST.get("features", "")
        navigation = request.POST.get("navigation")
        recommendation = request.POST.get("recommendation", "")

        try:
            Feedback.objects.create(
                name=name,
                email=email,
                rating=rating,
                discovery=discovery,
                features=features,
                navigation=navigation,
                recommendation=recommendation
            )
            return redirect('job_list')  # Redirect to a valid URL pattern
        except Exception as e:
            return render(request, "feedback.html", {'error': str(e)})
    return render(request, "feedback.html")


# def analytics_view(request):
#     user = request.user
    
#     # Count the total applications for the user
#     total_applications = Add_Job.objects.filter(user=user).count()
    
#     # Group applications by application_status (not status) and count them
#     applications_by_status = Add_Job.objects.filter(user=user).values('application_status').annotate(count=Count('application_status'))
    
#     # Group applications by job_category and count them
#     job_categories = Add_Job.objects.filter(user=user).values('job_category').annotate(count=Count('job_category'))
    
#     # Filter upcoming interviews
#     upcoming_interviews = Add_Job.objects.filter(user=user, interview_date__gte=timezone.now()).order_by('interview_date')

#     # Prepare context data to pass to the template
#     context = {
#         'total_applications': total_applications,
#         'applications_by_status': {item['application_status']: item['count'] for item in applications_by_status},
#         'job_categories': {item['job_category']: item['count'] for item in job_categories},
#         'upcoming_interviews': [{'interview_date': i.interview_date, 'company_name': i.company_name} for i in upcoming_interviews],
#     }

#     return render(request, 'analytics.html', context)
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.shortcuts import render
from .models import Add_Job
from django.db.models import Count

@login_required(login_url='/login/')  # Redirect to login page if not logged in
def analytics_view(request):
    user = request.user

    # Count the total applications for the user
    total_applications = Add_Job.objects.filter(user=user).count()

    # Group applications by application_status and count them
    applications_by_status = (
        Add_Job.objects.filter(user=user)
        .values('application_status')
        .annotate(count=Count('application_status'))
    )

    # Group applications by job_category and count them
    job_categories = (
        Add_Job.objects.filter(user=user)
        .values('job_category')
        .annotate(count=Count('job_category'))
    )

    # Filter upcoming interviews
    upcoming_interviews = (
        Add_Job.objects.filter(user=user, interview_date__gte=now())
        .order_by('interview_date')
    )

    # Prepare context data to pass to the template
    context = {
        'total_applications': total_applications,
        'applications_by_status': {item['application_status']: item['count'] for item in applications_by_status},
        'job_categories': {item['job_category']: item['count'] for item in job_categories},
        'upcoming_interviews': [
            {'interview_date': i.interview_date, 'company_name': i.company_name}
            for i in upcoming_interviews
        ],
    }

    return render(request, 'analytics.html', context)


def cards(request):
    return render(request, "card.html")


def profile_view(request):
    user = request.user  # Or however you're fetching the user
    return render(request, "profile.html", {'user': user})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, modelformset_factory
from django.db import transaction
from .models import UserProfile, SocialProfile, Skill, Project
from .forms import UserProfileForm, SocialProfileForm, SkillForm, ProjectForm

@login_required
def profile_form_add(request):
    user = request.user  
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    SocialProfileFormSet = inlineformset_factory(UserProfile, SocialProfile, form=SocialProfileForm, extra=3, max_num=3, can_delete=False)
    SkillFormSet = inlineformset_factory(UserProfile, Skill, form=SkillForm, extra=3, max_num=3 , can_delete=False)
    ProjectFormSet = inlineformset_factory(UserProfile, Project, form=ProjectForm, extra=3, max_num=3 , can_delete=False)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        social_formset = SocialProfileFormSet(request.POST, instance=user_profile)
        skill_formset = SkillFormSet(request.POST, instance=user_profile)
        project_formset = ProjectFormSet(request.POST, instance=user_profile)

        # 🔥 Exclude completely empty forms before validation
        def filter_valid_forms(formset):
            return [form for form in formset if form.has_changed()]  # Only keep changed forms

        valid_projects = filter_valid_forms(project_formset)

        # ✅ Check that valid forms don't exceed the max limit
        if len(valid_projects) > 3:
            for form in project_formset:
                form.add_error(None, "You can only have up to 3 projects.")

        # Print all the forms with error if occurs : 
        if not (profile_form.is_valid() and social_formset.is_valid() and skill_formset.is_valid() and project_formset.is_valid()):
            print("Form errors:", profile_form.errors)
            print("Social Form errors:", social_formset.errors)
            print("Skill Form errors:", skill_formset.errors)
            print("Project Form errors:", project_formset.errors)

        # if (profile_form.is_valid() and social_formset.is_valid() and 
        #     skill_formset.is_valid() and project_formset.is_valid()):
        #     with transaction.atomic():  # Ensures all or nothing is saved
        #         profile_form.save()
        #         social_formset.save()
        #         skill_formset.save()
        #         project_formset.save()
        #     return redirect('job_profile')  # Redirect to profile page after success
        if (profile_form.is_valid() and social_formset.is_valid() and 
            skill_formset.is_valid() and project_formset.is_valid()):
            
            print("✅ All forms are valid, entering transaction.atomic()")

            with transaction.atomic():  # Ensures all or nothing is saved
                profile_form.save()
                print("Profile form saved ✅")

                social_formset.save()
                print("Social formset saved ✅")

                skill_formset.save()
                print("Skill formset saved ✅")

                project_formset.save()
                print("Project formset saved ✅")

            print("✅ All forms saved successfully!")
            return redirect('job_profile')  # Redirect to profile page after success


    else:
        profile_form = UserProfileForm(instance=user_profile)
        social_formset = SocialProfileFormSet(instance=user_profile)
        skill_formset = SkillFormSet(instance=user_profile)
        project_formset = ProjectFormSet(instance=user_profile)

    return render(request, 'profile_form_add.html', {
        'profile_form': profile_form,
        'social_formset': social_formset,
        'skill_formset': skill_formset,
        'project_formset': project_formset
    })



## Profile View :
@login_required
def profile_view(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    
    social_profiles = SocialProfile.objects.filter(user_profile=user_profile)
    skills = Skill.objects.filter(user_profile=user_profile)
    projects = Project.objects.filter(user_profile=user_profile)

    return render(request, 'profile_view.html', {
        'user_profile': user_profile,
        'social_profiles': social_profiles,
        'skills': skills,
        'projects': projects,
    })

# ## Profile View :
# @login_required
# def job_profile_view(request):
#     user = request.user
#     user_profile = get_object_or_404(UserProfile, user=user)
    
#     social_profiles = SocialProfile.objects.filter(user_profile=user_profile)
#     skills = Skill.objects.filter(user_profile=user_profile)
#     projects = Project.objects.filter(user_profile=user_profile)
#     social_profiles = SocialProfile.objects.filter(user_profile=user_profile)

#     return render(request, 'job_profile.html', {
#         'user_profile': user_profile,
#         'social_profiles': social_profiles,
#         'skills': skills,
#         'projects': projects,
#         "social_profiles": social_profiles, 
#     })
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, SocialProfile, Skill, Project

@login_required
def job_profile_view(request):
    user = request.user
    
    # Try to fetch the UserProfile for the current user
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        # If no profile is found, redirect to profile creation page
        messages.error(request, "You do not have a profile. Please create one.")
        return redirect('profile_add')  # Change to the appropriate URL for creating a profile
    
    # Get associated data
    social_profiles = SocialProfile.objects.filter(user_profile=user_profile)
    skills = Skill.objects.filter(user_profile=user_profile)
    projects = Project.objects.filter(user_profile=user_profile)
    
    return render(request, 'job_profile.html', {
        'user_profile': user_profile,
        'social_profiles': social_profiles,
        'skills': skills,
        'projects': projects,
    })
