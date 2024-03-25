from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles


def index(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'title': 'Новости', 'news': news})

