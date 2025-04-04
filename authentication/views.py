from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from authentication.models import OTP
from authentication.utils import generate_otp, send_otp_to_users
from datetime import datetime, timedelta
from django.utils.timezone import now, make_aware, is_naive
# from django.contrib.au

from django.contrib.auth.models import User
from datetime import datetime

# @csrf_protect
def signup_view(request):
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # # Check if the username or email exists
        # user_by_username = User.objects.filter(username=username).first()
        # user_by_email = User.objects.filter(email=email).first()

        # if user_by_username and user_by_email:
        #     # Check if username and email belong to the same user
        #     if user_by_username != user_by_email:
        #         error = "Username and Email are already taken by different users. Please use unique credentials."
        #         return render(request, 'signup.html', {'error': error})
        # elif user_by_username:
        #     error = "Username already exists. Please choose a different one."
        #     return render(request, 'signup.html', {'error': error})
        # elif user_by_email:
        #     error = "Email already exists. Please use a different email."
        #     return render(request, 'signup.html', {'error': error})
        # Check if the username exists
        user_by_username = User.objects.filter(username=username).first()
        # Check if the email exists
        user_by_email = User.objects.filter(email=email).first()

        # If both username and email are taken by different users, return an error
        if user_by_username and user_by_email and user_by_username != user_by_email:
            error = "Username and email are already in use. Please choose another combination"
            return render(request, 'signup.html', {'error': error})

        # If only username exists, show an error
        elif user_by_username:
            error = "Username already exists. Please choose a different one."
            return render(request, 'signup.html', {'error': error})

        # If only email exists, show an error
        elif user_by_email:
            error = "Email already exists. Please use a different email."
            return render(request, 'signup.html', {'error': error})


        # Generate OTP and save user details temporarily in the session
        otp_code = generate_otp()
        request.session['temp_user_data'] = {
            'username': username,
            'email': email,
            'password': password,
            'otp_code': otp_code,
            'otp_timestamp': datetime.now().isoformat()  # Save the timestamp
        }

        # Send OTP to user's email
        title = 'Welcome to Career_Traces.com - Verify Your Account'
        
        message = f"""
Dear {username},

Welcome to Career_Traces.com! We're excited to have you on board.

To complete your registration, please verify your email address by entering the One-Time Password (OTP) provided below:

OTP Code: {otp_code}

This OTP will expire in 2 minutes. If you did not request this verification, please disregard this email.

Thank you for joining us!

Best regards,
Career_Traces.com Support Team
"""

        send_otp_to_users(title, message, email)  # Use the utility function

        # Redirect to OTP verification page
        return redirect('verify_otp')
    return render(request, 'signup.html')


def verify_otp_view(request):
    # Retrieve temporary user data from session
    temp_user_data = request.session.get('temp_user_data')

    if not temp_user_data:
        return redirect('signup')  # Redirect to signup if no session data exists

    otp_timestamp = temp_user_data['otp_timestamp']
    otp_timestamp = datetime.fromisoformat(otp_timestamp)

    # Ensure `otp_timestamp` is timezone-aware
    if is_naive(otp_timestamp):
        otp_timestamp = make_aware(otp_timestamp)

    # Calculate remaining time
    remaining_time = max(0, (otp_timestamp + timedelta(minutes=2) - now()).total_seconds())

    if request.method == 'POST':
        if 'resend_otp' in request.POST:
            # Generate and send a new OTP
            new_otp = generate_otp()
            temp_user_data['otp_code'] = new_otp
            temp_user_data['otp_timestamp'] = now().isoformat()
            request.session['temp_user_data'] = temp_user_data  # Update session data

            # Send the OTP via email
            email = temp_user_data['email']
            title = "Your New OTP Code"
            message = f"Your new OTP code is {new_otp}. It is valid for 2 minutes."
            send_otp_to_users(title, message, email)

            return render(request, 'verify_otp.html', {
                'info': 'A new OTP has been sent to your email.',
                'remaining_time': 120,  # Reset timer to 2 minutes
                'show_resend': False
            })

        # Combine OTP inputs into a single string
        otp_code = (
            request.POST.get('otp1', '') +
            request.POST.get('otp2', '') +
            request.POST.get('otp3', '') +
            request.POST.get('otp4', '') +
            request.POST.get('otp5', '') +
            request.POST.get('otp6', '')
        )

        # Handle OTP expiration
        if remaining_time <= 0:
            return render(request, 'verify_otp.html', {
                'error': 'OTP expired. Please resend a new OTP.',
                'remaining_time': 0,
                'show_resend': True  # Show the "Resend OTP" button
            })

        # Handle invalid OTP
        if otp_code != temp_user_data['otp_code']:
            return render(request, 'verify_otp.html', {
                'error': 'Invalid OTP. Please try again.',
                'remaining_time': int(remaining_time),
            })

        # Check if user already exists to avoid IntegrityError
        if User.objects.filter(email=temp_user_data['email']).exists():
            return render(request, 'verify_otp.html', {
                'error': 'An account with this email already exists. Please login.',
                'remaining_time': int(remaining_time)
            })

        # OTP verification successful
        user = User.objects.create_user(
            username=temp_user_data['username'],
            email=temp_user_data['email'],
            password=temp_user_data['password']
        )
        OTP.objects.create(user=user, otp_code=temp_user_data['otp_code'])
        del request.session['temp_user_data']  # Clear session data
        return redirect('login')

    # Render the OTP verification page with timer
    return render(request, 'verify_otp.html', {
        'remaining_time': int(remaining_time),
        'show_resend': remaining_time == 0  # Show "Resend OTP" button if time is up
    })


# Login View
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home_page')  # Redirect to home page after login
#         else:
#             error = 'Invalid credentials'
#             return render(request, 'login.html', {'error': error})
#     return render(request, 'login.html')
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from datetime import timedelta
from django.utils.timezone import now

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')  # Get remember me value

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            response = redirect('home_page')  # Redirect to home page

            if remember_me:  
                # Set session expiry to 30 days
                request.session.set_expiry(30 * 24 * 60 * 60)  
                response.set_cookie('remember_me', 'yes', max_age=30 * 24 * 60 * 60)  # 30 days
            else:
                request.session.set_expiry(0)  # Expires on browser close
            
            return response
        else:
            error = 'Invalid credentials'
            return render(request, 'login.html', {'error': error})
    
    return render(request, 'login.html')



# Forget Password View
def forget_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        # Check if the email exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'forget_password.html', {'error': 'Email not found'})
        
        # Generate OTP and save it
        otp_code = generate_otp()
        otp_timestamp = datetime.now().isoformat()  # Save timestamp in ISO format

        OTP.objects.update_or_create(
            user=user,
            defaults={'otp_code': otp_code, 'created_at': otp_timestamp}  # Save timestamp
        )
        
        # Send OTP to user's email
        title = 'Password Reset OTP for Career_Traces.com'
        
        message = f"""
Dear {user.username},

We received a request to reset the password for your account at Career_Traces.com.

To proceed with the reset, please enter the OTP below:

OTP Code: {otp_code}

This OTP will expire in 2 minutes. If you did not initiate this request, please ignore this email.

Best regards,
Career_Traces.com Support Team
"""

        send_otp_to_users(title, message, email)  # Use the utility function

        # Store user ID and OTP timestamp in session and redirect to OTP verification page
        request.session['reset_user_data'] = {
            'user_id': user.id,
            'otp_timestamp': otp_timestamp
        }
        return redirect('verify_reset_otp')
    return render(request, 'forget_password.html')


# OTP Verification for Password Reset
def verify_reset_otp_view(request):
    # Retrieve user data from session
    reset_user_data = request.session.get('reset_user_data')
    if not reset_user_data:
        return redirect('forget_password')  # Redirect if session data is missing

    user_id = reset_user_data['user_id']
    otp_timestamp = datetime.fromisoformat(reset_user_data['otp_timestamp'])

    # Ensure OTP timestamp is timezone-aware
    if is_naive(otp_timestamp):
        otp_timestamp = make_aware(otp_timestamp)

    # Calculate remaining time
    remaining_time = max(0, (otp_timestamp + timedelta(minutes=2) - now()).total_seconds())

    if request.method == 'POST':
        if 'resend_otp' in request.POST:
            # Generate and send a new OTP
            new_otp = generate_otp()
            reset_user_data['otp_timestamp'] = now().isoformat()
            request.session['reset_user_data'] = reset_user_data  # Update session data

            # Update OTP in database
            user = User.objects.get(id=user_id)
            OTP.objects.update_or_create(user=user, defaults={'otp_code': new_otp})

            # Send OTP via email
            title = 'Password Reset OTP for Career_Traces.com'
            # message = f"""
            #     Dear {user.username},

            #     Your new OTP code is {new_otp}. It is valid for 2 minutes.

            #     Best regards,
            #     Career_Traces.com Support Team
            # """
            message = f"""
Dear {user.username},

Your OTP for resetting your password is: {new_otp}. Please enter this code on the verification page.

This OTP will expire in 2 minutes.

Best regards,
Career_Traces.com Support Team
"""
            send_otp_to_users(title, message, user.email)

            return render(request, 'verify_otp.html', {
                'info': 'A new OTP has been sent to your email.',
                'remaining_time': 120,  # Reset timer to 2 minutes
                'show_resend': False
            })

        # Combine OTP inputs into a single string
        otp_code = (
            request.POST.get('otp1', '') +
            request.POST.get('otp2', '') +
            request.POST.get('otp3', '') +
            request.POST.get('otp4', '') +
            request.POST.get('otp5', '') +
            request.POST.get('otp6', '')
        )

        # Handle OTP expiration
        if remaining_time <= 0:
            return render(request, 'verify_otp.html', {
                'error': 'OTP expired. Please resend a new OTP.',
                'remaining_time': 0,
                'show_resend': True  # Show "Resend OTP" button
            })

        # Handle invalid OTP
        try:
            otp = OTP.objects.get(user_id=user_id, otp_code=otp_code)
            otp.delete()  # OTP matched, delete it
            request.session['reset_user_id'] = user_id  # Set reset_user_id in session
            del request.session['reset_user_data']  # Clear other session data
            return redirect('change_password')  # Redirect to password reset page
        except OTP.DoesNotExist:
            return render(request, 'verify_otp.html', {
                'error': 'Invalid OTP. Please try again.',
                'remaining_time': int(remaining_time),
            })

    # Render the OTP verification page with timer
    return render(request, 'verify_otp.html', {
        'remaining_time': int(remaining_time),
        'show_resend': remaining_time == 0  # Show "Resend OTP" button if time is up
    })


# Password Reset View
def change_password_view(request):
    error = ""
    success = ""
    user_id = request.session.get('reset_user_id')
    if not user_id:  # If reset_user_id is not in session
        return redirect('forget_password')  # Redirect to forget password page

    if request.method == 'POST':
        new_password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        
        if new_password != confirm_password:
            # If passwords do not match, return an error message
            error = 'Passwords do not match.'
            return render(request, 'change_password.html', {'error': error})
        try:
            # Update user password
            user = User.objects.get(id=user_id)
            user.set_password(new_password)
            user.save()
            
            # Clear session and redirect to login
            del request.session['reset_user_id']

            # Show success message in the template
            success = "Password Reset Successfully!"
        except User.DoesNotExist:
            error = "User does not exist. Please try again."
        
    return render(request, 'change_password.html', {'success': success, 'error': error})


def home_page(request):
    if request.user.is_authenticated:
        # Redirect authenticated users to the job list
        return redirect('job_list')
    # Render the home page for unauthenticated users
    return render(request, 'home_page.html')


# Logout View
# def logout_view(request):
#     logout(request)
#     return redirect("/")
def logout_view(request):
    response = redirect('login')  # Redirect to login page
    response.delete_cookie('remember_me')  # Delete remember_me cookie
    logout(request)
    return response


from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

