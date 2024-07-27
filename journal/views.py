from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm, ThoughtForm
# Create your views here.

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required


from django.contrib import messages

from  . models import Thought



def homepage(request):
    
    return render(request, 'journal/index.html' )

def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request, "User Created Successfully!")
            
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

@login_required(login_url='my_login')
def create_thought(request):
    
    
    form = ThoughtForm()
    
    
    if request.method == 'POST':
        
        form = ThoughtForm(request.POST)
        
        if form.is_valid():
            
            thought = form.save(commit=False)
            
            thought.user = request.user
            
            thought.save()
            
            return redirect('my_thoughts')
    
    context = {'CreateThoughtForm': form}
    
    return render(request, 'journal/create_thought.html',context)


@login_required(login_url='my_login')
def my_thoughts(request):
    
    current_user =  request.user.id
    
    thought = Thought.objects.all().filter(user=current_user)
    
    
    context = { 'AllThoughts': thought   }
    
    
    return render(request,'journal/my_thoughts.html', context )




