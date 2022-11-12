from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Article, Category, Message, Newsletter



# Create your views here.



def home(request):
    articles = Article.objects.all().order_by('-updated')
    recent = Article.objects.all().order_by('-updated')
    cat = Category.objects.all()
    for article in articles:
        category = article.category.all()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    if request.method == 'POST':
        email = request.POST.get('email')
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'شما قبلا عضو شده اید')
            return redirect('blog:home')
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, 'عضویت شما تایید شد')
            return redirect('blog:home')
    return render(request, 'Blog/index-7.html', {'articles': object_list, 'recent_article': recent, 'category': category, 'cat': cat, 'news': articles})


def detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'Blog/detail.html', {'article': article})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request,'Blog/result.html', {'articles': object_list})


def cat_lifestyle(request):
    article_lifestyle = Article.objects.filter(category=1)

    paginator = Paginator(article_lifestyle, 3)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    if request.method == 'POST':
        email = request.POST.get('email')
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'شما قبلا عضو شده اید')
            return redirect('blog:home')
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, 'عضویت شما تایید شد')
            return redirect('blog:home')
    return render(request, 'Blog/lifestyle.html', {'articles': object_list, 'news': article_lifestyle})


def cat_tech(request):
    article_technology = Article.objects.filter(category=2)
    paginator = Paginator(article_technology, 3)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    if request.method == 'POST':
        email = request.POST.get('email')
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'شما قبلا عضو شده اید')
            return redirect('blog:home')
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, 'عضویت شما تایید شد')
            return redirect('blog:home')
    return render(request, 'Blog/tech.html', {'articles': object_list, 'news': article_technology})


def cat_travel(request):
    article_travel = Article.objects.filter(category=3)
    paginator = Paginator(article_travel, 3)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    if request.method == 'POST':
        email = request.POST.get('email')
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'شما قبلا عضو شده اید')
            return redirect('blog:home')
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, 'عضویت شما تایید شد')
            return redirect('blog:home')
    return render(request, 'Blog/travel.html', {'articles': object_list, 'news': article_travel})


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
