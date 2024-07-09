from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm
# Create your views here.

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required



def homepage(request):
    
    return render(request, 'journal/index.html' )

def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('my_login')
            
    context = {'RegistrationForm': form} 
    
    return render(request, 'journal/register.html', context )


def my_login(request):
    
    form = LoginForm()
    
    if request.method == 'POST':
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)
            
            if user is not None:
                
                auth.login(request, user)
                
                return redirect('dashboard')
    
    context = {'LoginForm': form}
    
    return render(request, 'journal/my_login.html', context )

@login_required(login_url='my_login')
def dashboard(request):
    
    return render(request, 'journal/dashboard.html' )


def user_logout(request):
    
    auth.logout(request)
    
    return redirect("")
    