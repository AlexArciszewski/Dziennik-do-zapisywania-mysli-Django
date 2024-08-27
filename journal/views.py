from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm, ThoughtForm, UpdateUserForm, UpdateProfileForm
# Create your views here.

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


from django.contrib import messages

from  . models import Thought, Profile



def homepage(request):
    
    return render(request, 'journal/index.html' )

def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            current_user = form.save(commit=False)
            
            form.save()
            
            profile = Profile.objects.create(user=current_user)
            
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
    
    # profile_pic = Profile.objects.get(user=request.user)
    profile_pic, created = Profile.objects.get_or_create(user=request.user)
    context = {'profilePic': profile_pic }
    
    
    
    
    
    
    
    return render(request, 'journal/dashboard.html', context )


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



@login_required(login_url='my_login')
def update_thought(request, pk):
    
    try:
    
        thought = Thought.objects.get(id=pk, user =request.user)
    
    except:
        return redirect("my_thoughts.html")
    
    form = ThoughtForm(instance=thought)
    
    if request.method == 'POST':
        
        form = ThoughtForm(request.POST, instance=thought)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('my_thoughts')
    
    context = {'UpdateThought' : form}
    
    return render(request,'journal/update_thought.html', context)


@login_required(login_url='my_login')
def delete_thought(request, pk):
    
    try:
        thought = Thought.objects.get(id=pk, user =request.user)
    
    except:
        return redirect("my_thoughts.html")
    
    if request.method == 'POST':
        
        thought.delete()

        return redirect('my_thoughts')
    
    
    
    return render(request,'journal/delete_thought.html')




@login_required(login_url='my_login')
def profile_management(request):
    
    form = UpdateUserForm(instance=request.user)
    
    profile = Profile.objects.get(user=request.user)
    
    form_2 = UpdateProfileForm(instance=profile)
    
    
    if request.method == 'POST':
        
        form = UpdateUserForm(request.POST,instance=request.user)
        
        form_2 = UpdateProfileForm(request.POST,request.FILES, instance=profile)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('dashboard')
        
        if form_2.is_valid():
            
            form_2.save()
            
            return redirect('dashboard')
            
            
    context = {'UserUpdateForm': form, 'ProfileUpdateForm': form_2 }    
            
    return render(request,'journal/profile_management.html', context)        
          
            



@login_required(login_url='my_login')
def delete_account(request):
    
    if request.method == 'POST':
        
        deleteUser = User.objects.get(username=request.user)
        
        deleteUser.delete()
        
        return redirect("")
    
    
    return render(request,'journal/delete_account.html')  
    
    
    
    
    
    






