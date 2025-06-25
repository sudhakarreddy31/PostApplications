from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

# Create your views here.


def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'users/register.html',{'form':form})
