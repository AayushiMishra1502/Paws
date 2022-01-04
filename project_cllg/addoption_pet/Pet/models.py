
from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Pet(models.Model):
    PET_GENDER = (
        ('male','male'),
        ('female','female')
    )
    PET_CATEGORY = (
        ('Dog','Dog'),
        ('Cat','Cat'),
        ('Rabbit','Rabbit'),
    )
    PET_AGE = (
        ('Upto 6 months','Upto 6 months'),
        ('6-8 months','6-8 months'),
        ('1.5-3 years','1.5-3 years'),
        ('3 years or more','3 years or more'),
    )
    PET_YES_OR_NO = (
        ('Yes','Yes'),
        ('No','No'),
    )
    pet_category = models.CharField(max_length=50,choices=PET_CATEGORY)
    pet_name = models.CharField(max_length=10)
    pet_age = models.CharField(max_length=50,choices=PET_AGE)
    pet_bread = models.CharField(max_length=10)
    pet_gender = models.CharField(max_length=10,choices = PET_GENDER)
    pet_image = models.ImageField(upload_to = 'pePet_pic',default="", null=True, blank=True)
    pet_vaccinated = models.CharField(max_length=3,choices=PET_YES_OR_NO,default="")
    pet_neutered = models.CharField(max_length=3,choices=PET_YES_OR_NO,default="")
    pet_sprayed = models.CharField( max_length=3,choices=PET_YES_OR_NO,default="")
    pet_good_kids = models.CharField( max_length=3,choices=PET_YES_OR_NO,default="")

    def __str__(self):
        return f"{self.pet_category}-{self.pet_name}"
