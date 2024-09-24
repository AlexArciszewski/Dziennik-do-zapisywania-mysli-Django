from django.db import models
from django.contrib.auth.models import User

class Thought(models.Model):
    """Thought model"""
    
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=400)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, max_length=30, on_delete=models.CASCADE, null=True)


class Profile(models.Model):
    """Profile model"""
    
    profile_pic = models.ImageField(null=True, blank =True, default ='Default.png')
    user = models.OneToOneField(User, max_length=30, on_delete=models.CASCADE, null=True)



































