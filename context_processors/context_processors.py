from Blog.models import Article, Category

def Breakingnews(request):
    article = Article.objects.filter(category=4).order_by('-updated')
    return {'articles': article}

def more_news(request):
    news = Article.objects.all().order_by('?')
    return {'news': news}
