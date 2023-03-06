from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Article


def company(request):
    return HttpResponse('А тут раздел компании и он передает тебе пламенный приветик')

# Create your views here.

def index(request):
    latest_articles = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'articles/list.html', {'articles': latest_articles})

def detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Exception:
        return Http404('Статья не найдена!')
    return render(request, 'articles/article.html', {'article': article})

