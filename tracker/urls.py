from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', login_page, name="login"),  # Root URL shows the login page
    path('home/', home, name='home'),    # Home page
    path('login/', login_page, name='login'),  # Redundant but still useful if referenced directly
    path('signup/', signup_page, name='signup'),  # Signup page
    path('logout/', logout_view, name='logout'),
# New Path of Urls and add the view from Authentication Project:

    path('jobs/', job_list, name='job_list'),
    path('jobs/create/', job_create, name='job_create'),
    path('home/', home, name='home'),
    path('jobs/update/<int:job_id>/', job_update, name='job_update'),
    path('jobs/delete/<int:id>/', job_delete, name='job_delete'),
    # path('jobs/search/', search,name='search')
    path('jobs/search/', search, name='search'),
    path('jobs/profile/', profile, name='profile'),
    path('jobs/feedback/', feedback, name='feedback'),
    # path('jobs/analytics/', analytics_view, name='analytics')
    path('jobs/analytics/', analytics_view, name='simple_analytics'),


]
