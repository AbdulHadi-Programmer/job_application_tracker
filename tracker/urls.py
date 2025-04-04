from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from authentication.views import * 

urlpatterns = [
    path('', home_page, name='home'),  # uses the redirect logic for auth users
    path('login/', login_view, name='login'),
    path('home-page/', home_page_default, name="default"),

    path('logout/', logout_view, name='logout'),
    path('jobs/', job_list, name='job_list'),
    # path('jobs/create/', job_create, name='job_create'),
    # path('jobs/update/<int:job_id>/', job_update, name='job_update'),

    # URL for creating a new job
    path('jobs/create/', job_create_or_update, name='job_create_or_update'),
    # URL for updating a job
    path('jobs/update/<int:job_id>/', job_create_or_update, name='job_create_or_update'),


    path('jobs/delete/<int:id>/', job_delete, name='job_delete'),
    path('jobs/search/', search, name='search'), 
    # path('jobs/profile/', profile, name='profile'),
    path('jobs/feedback/', feedback, name='feedback'),
    path('jobs/delete/confirm/<int:id>/', job_delete_confirmation, name='job_delete_confirmation'),
    path('jobs/analytics/', analytics_view, name='simple_analytics'),
    path('jobs/card0124558454/', cards, name='cards'),
    path('jobs/profile/', profile, name='profile'),

    path('jobs/profile_view/', profile_view, name='profile_view'),
    path('jobs/job_dynamic_profile/', job_profile_view, name='job_profile'),

    path('profile/add/', profile_form_add, name='profile_add'),  # Add Profile
    path('profile/edit/', profile_form_add, name='profile_edit'),  # Edit Profile (Same view)

]
