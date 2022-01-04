from .models import Pet
from . import views
from django.urls import path
from .views import Profile

urlpatterns = [
    path('',views.index, name='pet_index'),
    path('pet_reg/',views.pet_reg, name='pet_reg'),
    path('pet_index/',views.index, name='pet_index'),
    path('pet_profile/<int:pk>',Profile.as_view(), name='pet_profile'),
]


