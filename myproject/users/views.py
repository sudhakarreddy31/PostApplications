from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required 
# Create your views here.


def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'users/register.html',{'form':form})


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request,user)
                return redirect('profile')
    return render(request, 'users/login.html',{'form':form})

@login_required
def logout_view(request):
    logout(request)
    return render('login')

@login_required(login_url ='login')                            # if want profile urls in wensite write this peice of code @login_required(login_url = 'profile')
def profile_view(request):
    return render(request, 'users/profile.html')