from django.shortcuts import render
from blog.models import Category, Article

def list(request):
    articulos = Article.objects.all()
    return render(request, 'articles/list.html', {
        'title': "Articulos"
        'articles': articles
    })