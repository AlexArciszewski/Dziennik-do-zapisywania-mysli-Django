
"""
URL configuration for edenthought project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views



urlpatterns = [
    
    path("", views.homepage, name=""),
    
    path("register", views.register, name="register"),
    
    path("my_login", views.my_login, name="my_login"),
    
    path("dashboard", views.dashboard, name="dashboard"),
    
    path("user_logout", views.user_logout, name="user_logout"),
    
    path("create_thought", views.create_thought, name="create_thought"),
    
    path("my_thoughts", views.my_thoughts, name="my_thoughts"),
    
    path("update_thought/<str:pk>", views.update_thought, name="update_thought"),
    
    path("delete_thought/<str:pk>", views.delete_thought, name="delete_thought"),
    
    path("profile_management", views.profile_management, name="profile_management"),
    
]













