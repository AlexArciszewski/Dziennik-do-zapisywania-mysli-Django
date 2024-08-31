
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

from django.contrib.auth import views as auth_views


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
    
    path("delete_account", views.delete_account, name="delete_account"),
    
    
    #  Password management
    #  1 urls pozwalajacy na wejscie do naszego maila w celu uzyskania hasła
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="journal/password-reset.html"),name="reset_password"),
    
    #  2 urls pozwalajacy na wyświetlenie wiadomosci o sukcesie połączenia i wysłania maila resetujacego haslow
    
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="journal/password-reset-sent.html"),name="password_reset_done"),
 
    # 3 url pozwalający wsyłać linka na nasz adres email dzieki czemu możliwy jest reset hasła
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="journal/password-reset-form.html"), name="password_reset_confirm"),
    
    #  4 url pokaż informacje o sukcesie zmiany hasła
    
    path('pasword_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="journal/password-reset-complete.html"), name="password_reset_complete"),
    
    
]   













