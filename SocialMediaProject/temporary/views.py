from django.shortcuts import render
from django.http import HttpResponse


menu = ['Товарищи', 'Сообщения', 'Форум', 'Контакты']


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu
    }
    return render(request, 'temporary/index.html', context=data)


def about(request):
    return render(request, 'temporary/about.html', {'title': 'Контакты'})


def messages(request):
    return render(request, 'temporary/messages.html', {'title': 'Сообщения'})


def comrades(request):
    return render(request, 'temporary/friends.html', {'title': 'Товарищи'})


def forum(request):
    return render(request, 'temporary/forum.html', {'title': 'Форум'})
