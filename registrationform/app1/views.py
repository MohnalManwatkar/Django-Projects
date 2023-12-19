from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

# Authenticate function model
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

def homePage(request):
    return render(request, 'homePage.html')

def registrationPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'registrationPage.html', {'form':form})


# login with authenticate page

def my_loginPage(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            #creating a user and authenticating the details
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
        
    return render(request, 'my_loginPage.html', {'form':form})

# logout page

def user_logoutPage(request):
    auth.logout(request)
    return redirect('')


@login_required(login_url="login")
def dashboardPage(request):
    return render(request, 'dashboardPage.html')