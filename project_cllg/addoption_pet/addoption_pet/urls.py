from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Pet.urls')),
    path('pet_reg/',include('Pet.urls')),
    path('pet_index/',include('Pet.urls')),
    path('pet_profile/',include('Pet.urls'))
]
