from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method=="POSt":
        if request.POST['password']==request.POST['repeat']:
            new_user=User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, new_user)
            return redirect('home')
        
    return render(request, 'register.html')
