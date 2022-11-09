from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Article, Category, Message, Newsletter


# Create your views here.


def home(request):
    articles = Article.objects.all().order_by('?')
    recent = Article.objects.all().order_by('-updated')
    cat = Category.objects.all()
    for article in articles:
        category = article.category.all()

    if request.method == 'POST':
        email = request.POST.get('email')
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'شما قبلا عضو شده اید')
            return redirect('blog:home')
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, 'عضویت شما تایید شد')
            return redirect('blog:home')
    return render(request, 'Blog/index-7.html', {'articles': articles, 'recent_article': recent, 'category': category, 'cat': cat})


def detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'Blog/detail.html', {'article': article})


def cat_lifestyle(request):
    article_lifestyle = Article.objects.filter(category=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'شما قبلا عضو شده اید')
            return redirect('blog:home')
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, 'عضویت شما تایید شد')
            return redirect('blog:home')
    return render(request, 'Blog/lifestyle.html', {'articles': article_lifestyle})


def cat_tech(request):
    article_technology = Article.objects.filter(category=2)
    if request.method == 'POST':
        email = request.POST.get('email')
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'شما قبلا عضو شده اید')
            return redirect('blog:home')
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, 'عضویت شما تایید شد')
            return redirect('blog:home')
    return render(request, 'Blog/tech.html', {'articles': article_technology})


def cat_travel(request):
    article_travel = Article.objects.filter(category=3)
    if request.method =='POST':
        email = request.POST.get('email')
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'شما قبلا عضو شده اید')
            return redirect('blog:home')
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, 'عضویت شما تایید شد')
            return redirect('blog:home')
    return render(request, 'Blog/travel.html', {'articles': article_travel})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('msg_subject')
        body = request.POST.get('message')
        Message.objects.create(name=name, email=email, title=title, body=body)
        messages.success(request, 'پیام شما با موفقیت ارسال شد')
        return render(request, 'Blog/contact.html')
    return render(request, 'Blog/contact.html')


def signin(request):
    if request.user.is_authenticated:
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


def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        Newsletter.objects.create(email=email)
        messages.success(request, 'عضویت شما تایید شد')

    return render(request, 'includes/newsletter.html')
