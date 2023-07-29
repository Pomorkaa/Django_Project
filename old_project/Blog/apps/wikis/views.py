from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404
from .models import Wiki

def index(request):
    latest_wiki = Wiki.objects.order_by('-wiki_date')[:10]
    return render(request, 'Wikis/list.html', {'wiki': latest_wiki})

def detail(request, wiki_id):
    try:
        wiki = Wiki.objects.get(id=wiki_id)
    except Exception:
        return Http404('Инструкция не найдена!')
    return render(request, 'wikis/wiki.html', {'wiki': wiki})



