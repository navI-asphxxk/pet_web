from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')


def reviews(request):
    return HttpResponse('Отзывы')


def custom(request):
    return HttpResponse('Custom')


def custom_pc(request):
    return HttpResponse('PC')


def custom_device(request):
    return HttpResponse('DEVICE')


def dev(request):
    return HttpResponse('DEVELoper')


def web_dev(request):
    return HttpResponse('WEB')


def bot_dev(request):
    return HttpResponse('BOT')


@login_required()
def profile(request):
    return render(request, 'main/profile.html')


def feedback(request):
    return HttpResponse("Feedback")