from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        uname=request.POST['uname']
        pass1=request.POST['pass1']
        user=User.objects.create_user(username=uname, password=pass1)
        user.save()
        return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        uname=request.POST['uname']
        pass1=request.POST['pass1']
        user= auth.authenticate(username=uname, password=pass1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print ("invalid")
            return redirect('login')          
            
    return render(request, 'login.html')
