from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from authentication.views import * 

# urlpatterns = [
#     path('', login_view, name='login'),
#     path('home/', home, name='home'),
#     path('signup/', signup_view, name='signup'),
#     path('verify-otp/', verify_otp_view, name='verify_otp'),
#     path('forget_password/', forget_password_view, name='forget_password'),
#     path('verify_reset_otp/', verify_reset_otp_view, name='verify_reset_otp'),
#     path('change_password/', change_password_view, name='change_password'),
#     path('logout/', logout_view, name='logout'),
#     path('jobs/', job_list, name='job_list'),
#     path('jobs/create/', job_create, name='job_create'),
#     path('jobs/update/<int:job_id>/', job_update, name='job_update'),
#     path('jobs/delete/<int:id>/', job_delete, name='job_delete'),
#     path('jobs/search/', search, name='search'),
#     path('jobs/profile/', profile, name='profile'),
#     path('jobs/feedback/', feedback, name='feedback'),
#     path('jobs/analytics/', analytics_view, name='simple_analytics'),
#     path('jobs/card', cards, name='cards')
# ]

## Correct all urls and also :
# urlpatterns = [
#     path('', login_view, name='login'),
#     path('home/', home, name='home'),  # uses the redirect logic for auth users
#     path('logout/', logout_view, name='logout'),
#     path('jobs/', job_list, name='job_list'),
#     path('jobs/create/', job_create, name='job_create'),
#     path('jobs/update/<int:job_id>/', job_update, name='job_update'),
#     path('jobs/delete/<int:id>/', job_delete, name='job_delete'),
#     path('jobs/search/', search, name='search'),
#     path('jobs/profile/', profile, name='profile'),
#     path('jobs/feedback/', feedback, name='feedback'),
#     path('jobs/analytics/', analytics_view, name='simple_analytics'),
#     path('jobs/card', cards, name='cards'),

# ]

urlpatterns = [
    path('', home_page, name='home'),  # uses the redirect logic for auth users
    path('login/', login_view, name='login'),
    
    path('logout/', logout_view, name='logout'),
    path('jobs/', job_list, name='job_list'),
    path('jobs/create/', job_create, name='job_create'),
    path('jobs/update/<int:job_id>/', job_update, name='job_update'),
    path('jobs/delete/<int:id>/', job_delete, name='job_delete'),
    path('jobs/search/', search, name='search'),
    path('jobs/profile/', profile, name='profile'),
    path('jobs/feedback/', feedback, name='feedback'),
    path('jobs/analytics/', analytics_view, name='simple_analytics'),
    path('jobs/card', cards, name='cards'),
    
]
