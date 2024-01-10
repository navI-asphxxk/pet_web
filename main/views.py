from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Проверка")

def about(request):
    return HttpResponse("about")
