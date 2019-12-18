from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Author
# Create your views here.

def register(request):
    registered = 0
    if request.method == 'POST':
        #print("view hit!")
        username = request.POST.get('username')
        if username_present(username):
            registered = 1
        else:    
            password = request.POST.get('password')
            f_name = request.POST.get('firstname')
            l_name = request.POST.get('lastname')
            email = request.POST.get('email')
            user = User.objects.create_user(username=username, email=email, password=password)
            Author.objects.create(user = user, first_name=f_name, last_name=l_name)
            registered = 2
    return render(request, 'users/signup.html', {'registered':registered})

def username_present(username):
    if User.objects.filter(username=username).exists():
        return True
    return False

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    return render(request, 'users/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')
    