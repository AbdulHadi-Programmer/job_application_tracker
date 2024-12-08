# This is a function to search a job 
# views.py
import json
from .forms import FeedbackForm
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

@login_required
# def home(request):
#     return redirect(request, 'job_list')
def home(request):
    if request.user.is_authenticated:
        return redirect('job_list')
    return redirect('login')

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

    context = {
        'jobs': jobs,
        'all_emails_empty': all_emails_empty,  # Pass the flag to the template
    }
    return render(request, 'job_list.html', context)




@login_required # (with Foreign Key new code)
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user  # Automatically assign the current user
            job.save()
            messages.success(request, 'Job created successfully!')
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'job_form.html', {'form': form})



@login_required # (with Foreign Key new code)
def job_update(request, job_id):
    job = get_object_or_404(Add_Job, id=job_id, user=request.user)  # Ensure the job belongs to the current user
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'job_update.html', {'form': form, 'job': job})


@login_required
def job_delete(request, id):
    job = get_object_or_404(Add_Job, id=id, user=request.user)  # Ensure the job belongs to the current user
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('job_list')
    
    return render(request, 'job_list.html', {'job': job})


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
                data = data.filter(Add_Job(job_category__icontains=job_category))  # Partial match

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
    return render(request, "user_profile.html")




@login_required
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the feedback to the database
            return redirect('job_list')  # Redirect after saving
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})



def analytics_view(request):
    user = request.user
    
    # Count the total applications for the user
    total_applications = Add_Job.objects.filter(user=user).count()
    
    # Group applications by application_status (not status) and count them
    applications_by_status = Add_Job.objects.filter(user=user).values('application_status').annotate(count=Count('application_status'))
    
    # Group applications by job_category and count them
    job_categories = Add_Job.objects.filter(user=user).values('job_category').annotate(count=Count('job_category'))
    
    # Filter upcoming interviews
    upcoming_interviews = Add_Job.objects.filter(user=user, interview_date__gte=timezone.now()).order_by('interview_date')

    # Prepare context data to pass to the template
    context = {
        'total_applications': total_applications,
        'applications_by_status': {item['application_status']: item['count'] for item in applications_by_status},
        'job_categories': {item['job_category']: item['count'] for item in job_categories},
        'upcoming_interviews': [{'interview_date': i.interview_date, 'company_name': i.company_name} for i in upcoming_interviews],
    }

    return render(request, 'analytics.html', context)

def cards(request):
    return render(request, "card.html")