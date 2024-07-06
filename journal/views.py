from django.shortcuts import render, redirect

from . forms import CreateUserForm
# Create your views here.


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
    
    return render(request, 'journal/my_login.html' )



def dashboard(request):
    
    return render(request, 'journal/dashboard.html' )

