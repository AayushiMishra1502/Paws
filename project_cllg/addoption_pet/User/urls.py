from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reg/',views.User_reg, name='user_reg'),
    path('login/', auth_views.LoginView.as_view(template_name='User/login.html'), name= 'login'),
    path('logout/',views.log_out ,name='logout'),
    path('profile/',views.profile, name='user_profile'),
]


