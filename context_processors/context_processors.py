from Blog.models import Article, Category


def Breakingnews(request):
    breaking_news = Article.objects.filter(category=4).order_by('-updated')
    return {'breaking_news': breaking_news}


def more_news(request):
    news = Article.objects.all().order_by('?')
    return {'news': news}
