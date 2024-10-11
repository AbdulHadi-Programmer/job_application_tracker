from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
    path('login/', login_page, name='login'),
    
    # path('logout/',custom_logout, name='logout'),
    path('jobs/', job_list, name='job_list'),
    path('jobs/create/', job_create, name='job_create'),
    path('home/', home, name='home'),
    path('jobs/update/<int:job_id>/', job_update, name='job_update'),
    path('jobs/delete/<int:id>/', job_delete, name='job_delete'),

    # path('', auth_views.LoginView.as_view(), name='login'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
