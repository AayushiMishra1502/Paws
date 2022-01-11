from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,CreateView

# Create your views here.
context = {'pets':Pet.objects.all()}
    

class PetCreateView(LoginRequiredMixin,CreateView):
    model= Pet
    fields = ['pet_name','pet_category','pet_age','pet_bread','pet_gender','pet_image','pet_vaccinated','pet_neutered','pet_sprayed','pet_good_kids','pet_address']
    
    def form_valid(self, form) :
     print('check')
     print(Pet.pet_owner)
     print(self.request.user)
     form.instance.pet_owner=self.request.user  
     return super().form_valid(form)

class PetDetailView(DetailView):
    model = Pet
    template_name='Pet/pet_detail.html'
    

@login_required
def Pet_Home(request):
    return render(request,'Pet/pet_home.html',context)

@login_required
def Pet_Home_dog(request):
    return render(request,'Pet/pet_dog.html',context)

@login_required
def Pet_Home_cat(request):
    return render(request,'Pet/pet_cat.html',context)

@login_required
def search(request):
    return render(request,'Pet/pet_search.html')