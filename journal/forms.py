from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import  User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from .models import Thought, Profile


class CreateUserForm(UserCreationForm):
    """User class"""
    
    class Meta:
        """meta class with user class spec"""
        
        model = User
        fields = ["username", "email", "password1", "password2" ]
        
        
class LoginForm(AuthenticationForm):
    """Login form class"""
    
    username  = forms.CharField(widget=TextInput())
    password =  forms.CharField(widget=PasswordInput())  
    
    
class ThoughtForm(ModelForm):
    
    class Meta:
        model = Thought
        fields = ['title', 'content',]
        exclude =['user',]

        
class UpdateUserForm(forms.ModelForm):
    
    password = None
    
    class Meta:
        
        model = User
        
        fields = ["username", "email", ]    
        exclude = ["password1", "password2", ] 
        
        
        
class UpdateProfileForm(forms.ModelForm):   
    """update form class"""
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))
    
    class Meta:
        """spec for profile"""
        
        model = Profile
        fields = ['profile_pic',]