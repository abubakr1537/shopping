from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm):
    COLOR = (
        ('white','white'),
        ('black','black')
    )

    CATEGORY = (
        ('electronics','electronics'),
        ('clothes','clothes'),
        ('shoes','shoes'),
        ('household','household')
    )

    name = forms.CharField(max_length=255)
    price = forms.DecimalField(max_digits=100, decimal_places=2)
    description = forms.CharField(
        max_length=2000,
        widget = forms.Textarea()
    )
    color = forms.ChoiceField(choices=COLOR)
    category = forms.ChoiceField(choices=CATEGORY)
    
    class Meta:
        model = Products
        fields = ['name','price','description','color','category','image',]

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)