from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.


def home(request):
    return render(request, 'Blog/index-7.html')


def cat_lifestyle(request):
    return render(request, 'Blog/lifestyle.html')


def cat_tech(request):
    return render(request, 'Blog/tech.html')


def cat_travel(request):
    return render(request, 'Blog/travel.html')


def contact(request):
    return render(request, 'Blog/contact.html')


def signin(request):
    if request.user.is_authenticated == True:
        return redirect('blog:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user, )
        if user is not None:
            login(request, user)
            return redirect('blog:home')
    return render(request, 'Blog/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('blog:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = User.objects.create(username=username, email=email, password=password1)
        login(request, user)
        return redirect('blog:home')
    return render(request, 'Blog/signup.html')


def user_logout(request):
    logout(request)
    return redirect('blog:home')