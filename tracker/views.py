from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .models import Add_Job, User
from .forms import JobForm

# View for the signup page
# def signup_page(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
        
#         # Create user using your custom manager
#         user = User.objects.create_user(username=username, email=email, password=password)
        
#         return redirect('job_list')  # Redirect to a success page or login page
#     return render(request, 'signup.html')

def signup_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Create user using your custom manager
        user = User.objects.create_user(username=username, email=email, password=password)
        
        return redirect('job_list')  # Redirect to a success page or login page
    return render(request, 'signup.html')

# Working but the redirection page is also login
####################################################
# def login_page(request):
#     if request.user.is_authenticated:
#         return redirect('home')  # Redirect to home if already logged in

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)  # Authenticate user

#         if user is not None:
#             login(request, user)  # Log in the user
#             # next_url = request.GET.get('next', 'job_list')  # Redirect to the intended page (default: job list)
#             next_url = request.POST.get('next') or 'job_list'  # Check POST data first
#             return redirect(next_url)
#         else:
#             messages.error(request, 'Invalid username or password.')  # Error message
#     return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_page(request):
    # if request.user.is_authenticated:
    #     return redirect('home')  # Redirect to home if already logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # Authenticate user

        # if user is not None:
        #     login(request, user)  # Log in the user
        #     next_url = request.POST.get('next') or 'job_list'  # Redirect to the intended page
        #     return redirect(next_url)
        # else:
        #     messages.error(request, 'Invalid username or password.')  # Error message
        if user is not None:
            login(request, user)
            return redirect('home')  # redirect to the home page or dashboard
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
    # return render(request, 'job_list.html')



# View for the home page (redirects to job_list if logged in)
@login_required
def home(request):
    return redirect('job_list')

# Oldest Function:-
@login_required
def job_list(request):
    if request.user.is_authenticated:
        jobs = Add_Job.objects.all()  # List all jobs, even if the user is authenticated
        return render(request, 'job_list.html', {'jobs': jobs})
    else:
        return redirect('login')

@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job created successfully!')
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'job_form.html', {'form': form})

@login_required
def job_update(request, job_id):
    job = get_object_or_404(Add_Job, id=job_id)
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
    job = get_object_or_404(Add_Job, id=id)
    if request.method == 'POST':
        job.delete()    
        messages.success(request, 'Job deleted successfully!')
        return redirect('job_list')
    return render(request, 'job_list.html', {'job': job})


