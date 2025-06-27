from django.shortcuts import render
from . models import InformationForm
from . forms import DataForm
from django.contrib import messages
# Create your views here.

def dynamic_form(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfuly Submitted")
        else:
            messages.error(request, "invalid Errors..")
    else:
        form = DataForm()
    return render(request,'dynamicforms/forms.html',{'form':form})
