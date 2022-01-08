from .models import Pet
from . import views
from django.urls import path
from .views import Profile

urlpatterns = [
    path('',views.index, name='pet_index'),
    path('pet_reg/',views.pet_reg, name='pet_reg'),
    path('pet_index/',views.index, name='pet_index'),
    path('pet_profile/',Profile.as_view(), name='pet_profile'),
    path('pet_home/',views.Pet_Home, name='pet_home'),
    path('pet_home_dog/',views.Pet_Home_dog, name='pet_home_dog'),
    path('pet_home_cat/',views.Pet_Home_cat, name='pet_home_cat'),
    path('about/',views.About, name='about'),
]


