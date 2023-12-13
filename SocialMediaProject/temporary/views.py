from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'temporary/index.html', {'title': 'Главная страница'})


def about(request):
    return HttpResponse('Контакты')
