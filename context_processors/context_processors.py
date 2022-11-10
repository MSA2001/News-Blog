from Blog.models import Article, Category

def Breakingnews(request):
    article = Article.objects.filter(category=4).order_by('-updated')
    return {'article': article}
