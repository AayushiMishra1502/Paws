from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Form 
from .models import Pet
from django.views.generic import DetailView

# Create your views here.
context = {'pets':Pet.objects.all()}


def pet_reg(request):
    print(request)
    pet_form = Form()
    if request.method == 'POST':
        pet_form = Form(request.POST)
        if pet_form.is_valid():
            print('TRUE')
            pet_form.save()
            messages.success(request,'you have account has been created !!you are now able to log in ')
            redirect('pet_index')
        else:
            print('FALSE')
    return render(request,"Pet/Pet_Reg.html",{'form':pet_form}) 

def index(request):
    return render(request,'Pet/index.html',context)


class Profile(DetailView):
    model = Pet
    template_name='pet_profile.html'
    
# def User(request):
#     return render(request,'Pet/user_register.html')

def Pet_Home(request):
    return render(request,'Pet/pet_home.html',context)

def Pet_Home_dog(request):
    return render(request,'Pet/pet_dog.html',context)

def Pet_Home_cat(request):
    return render(request,'Pet/pet_cat.html',context)

def About(request):
    return render(request,'Pet/about.html')