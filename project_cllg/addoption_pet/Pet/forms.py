from django.forms import ModelForm
from Pet.models import Pet


class Form(ModelForm):

    class Meta:
        model = Pet
        fields = '__all__'
