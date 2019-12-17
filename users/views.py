from django.shortcuts import render
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