from django.shortcuts import render

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