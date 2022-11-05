from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'Blog/index-7.html')

def cat_lifestyle(request):
    return render(request, 'Blog/post-category-3.html')
