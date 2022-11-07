from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Article


# Create your views here.


def home(request):
    articles = Article.objects.all().order_by('?')
    return render(request, 'Blog/index-7.html', {'articles': articles})



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
        else:
            messages.error(request, 'نام کاربری یا رمز شما اشتباه است')
    return render(request, 'Blog/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('blog:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'این نام کاربری از قبل وجود دارد')
            return render(request, 'Blog/signup.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'این ایمیل از قبل وجود دارد')
            return render(request, 'Blog/signup.html')

        if password1 != password2:
            messages.error(request, 'پسورد شما تطابق ندارد')
            return render(request, 'Blog/signup.html')
        user = User.objects.create(username=username, email=email, password=password1)
        login(request, user)
        return redirect('blog:home')
    return render(request, 'Blog/signup.html')


def user_logout(request):
    logout(request)
    return redirect('blog:home')