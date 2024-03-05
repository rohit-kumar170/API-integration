from django.shortcuts import render
from .forms import Registerform
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    form=Registerform(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'register.html',context={'form':form})
