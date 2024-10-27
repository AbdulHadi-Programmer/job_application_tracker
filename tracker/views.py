from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .models import Add_Job, User
from .forms import JobForm 

# This is old code working perfectly but it always redirected to login :
# def signup_page(request):
#     error = ""
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirmpassword')
        
#         if password != confirm_password:
#             error = "The passwords you entered do not match. Please ensure both fields contain the same password."

#         elif User.objects.filter(username=username).exists():
#             error = "Username is already taken. Please choose a different username."
        
#         elif User.objects.filter(email=email).exists():
#             error = "Email is already in use. Please choose a different email."
        
#         else:
#             user_data = User.objects.create_user(username=username, email=email, password=password)
#             user_data.save()
#             return redirect('/home')

#     return render(request, "signup.html", {'error': error})

# This is also perfectly working and correctly redirectly to direct home page but this is not for official launch:
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect

# def signup_page(request):
#     error = ""
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirmpassword')
        
#         if password != confirm_password:
#             error = "The passwords you entered do not match. Please ensure both fields contain the same password."

#         elif User.objects.filter(username=username).exists():
#             error = "Username is already taken. Please choose a different username."
        
#         elif User.objects.filter(email=email).exists():
#             error = "Email is already in use. Please choose a different email."
        
#         else:
#             # Create the user
#             user_data = User.objects.create_user(username=username, email=email, password=password)
#             user_data.save()
            
#             # Authenticate and log in the user
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/home')
#             else:
#                 error = "Something went wrong. Please try again."
#     return render(request, "signup.html", {'error': error})
# views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignupForm

def signup_page(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            full_name = form.cleaned_data['full_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            job_title = form.cleaned_data['job_title']
            company_name = form.cleaned_data['company_name']
            country = form.cleaned_data['country']
            
            
            if User.objects.filter(username=username).exists():
                error = "Username is already taken. Please choose a different username."
        
            elif User.objects.filter(email=email).exists():
                error = "Email is already in use. Please choose a different email."
        
            # Create the user
            user_data = User.objects.create_user(username=username, email=email, password=password)
            user_data.full_name = full_name  # Assuming you have a profile model for additional fields
            user_data.save()

            # Optionally, save additional fields in a Profile model
            # Profile.objects.create(user=user_data, job_title=job_title, company_name=company_name, country=country)

            # Authenticate and log in the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
            # else:
                # error = form.errors.as_json()  # Display errors if form is invalid
            return render(request, "signup.html", {'form': form, 'error': error})
    else:
        form = SignupForm()
    return render(request, "signup.html", {'form': form})




def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    error = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')   
        else:
            error = "Username or Password is Invalid"

    return render(request, 'login.html', {'error':error})



# View for the home page (redirects to job_list if logged in)
@login_required
def home(request):
    return redirect('job_list')


# Oldest Function:-
# @login_required
# def job_list(request):
#     if request.user.is_authenticated:
#         jobs = Add_Job.objects.all()  # List all jobs, even if the user is authenticated
#         return render(request, 'job_list.html', {'jobs': jobs})
#     else:
#         return redirect('login')

# New with foreign key added:
# @login_required
# def job_list(request):
#     if request.user.is_authenticated:
#         jobs = Add_Job.objects.filter(user=request.user)  # List all jobs, even if the user is authenticated
#         return render(request, 'job_list.html', {'jobs': jobs})
#     else:
#         return redirect('login')

# @login_required
# def job_list(request):
#     # Filter jobs by the current logged-in user
#     jobs = Add_Job.objects.filter(user=request.user).order_by("-interview_date")  
#     print(request.user)   
#     context = {
#         'jobs': jobs,
#     }
# #     return render(request, 'job_list.html', context)
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from .models import Add_Job

# @login_required
# def job_list(request):
#     # Filter jobs by the logged-in user
#     jobs = Add_Job.objects.filter(user=request.user).order_by("-interview_date")
    
#     # Capture search query (if available)
#     job_category = request.GET.get('job_category')

#     # Apply search filter if a category is provided
#     if job_category:
#         jobs = jobs.filter(job_category__icontains=job_category)  # Use 'icontains' for partial match

#     context = {
#         'jobs': jobs,
#     }
#     return render(request, 'job_list.html', context)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Add_Job

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
    logout(request)  # This will log out the user
    return redirect('login')  # Redirect the user to the login page after logout

def email_template(request):
    if request.method == 'POST':
        # emails = Add_Emai
        pass


######################################################################################################################################
# This is a function to search a job 
from django.shortcuts import render

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

from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm
from .models import Feedback



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


# @login_required
# def simple_analytics(request):
#     return render(request, 'simple_analytics.html')

# from collections import Counter
# from datetime import date

# def analytics_view(request):
#     total_applications = Add_Job.objects.count()

#     # Count applications by status
#     applications_by_status = Counter(Add_Job.objects.values_list('application_status', flat=True))

#     # Count job categories
#     job_categories = Counter(Add_Job.objects.values_list('job_category', flat=True))

#     # Get upcoming interviews
#     upcoming_interviews = Add_Job.objects.filter(interview_date__gte=date.today()).order_by('interview_date')

#     context = {
#         'total_applications': total_applications,
#         'applications_by_status': applications_by_status,
#         'job_categories': job_categories,
#         'upcoming_interviews': upcoming_interviews,
#     }

#     return render(request, 'analytics.html', context)

# Nothing could be changed:
# from collections import Counter 
# from datetime import date

# def analytics_view(request):
#     total_applications = Add_Job.objects.filter(user=request.user).count()  # Filter by user

#     # Count applications by status for the logged-in user
#     applications_by_status = Counter(Add_Job.objects.filter(user=request.user)
#                                      .values_list('application_status', flat=True))

#     # Count job categories
#     job_categories = Counter(Add_Job.objects.filter(user=request.user)
#                              .values_list('job_category', flat=True))

#     # Get upcoming interviews for the user
#     upcoming_interviews = Add_Job.objects.filter(user=request.user, 
#                                                  interview_date__gte=date.today()).order_by('interview_date')

#     context = {
#         'total_applications': total_applications,
#         'applications_by_status': dict(applications_by_status),  # Convert to dict
#         'job_categories': dict(job_categories),  # Convert to dict
#         'upcoming_interviews': upcoming_interviews,
#     }

#     return render(request, 'analytics.html', context)

# from collections import Counter
# from datetime import date
# from django.core.serializers.json import DjangoJSONEncoder
# from django.http import JsonResponse
import json
from django.shortcuts import render
from django.db.models import Count  # Ensure Count is imported
from django.utils import timezone  # Ensure timezone is imported

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
