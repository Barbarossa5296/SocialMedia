from django.shortcuts import render
from django.http import HttpResponse


menu = ['Товарищи', 'Сообщения', 'Форум', 'О сайте']


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu
    }
    return render(request, 'temporary/index.html', context=data)


def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu
    }
    return render(request, 'temporary/about.html', context=data)


def messages(request):
    data = {
        'title': 'Сообщения',
        'menu': menu
    }
    return render(request, 'temporary/messages.html', context=data)


def contacts(request):
    data = {
        'title': 'Контакты',
        'menu': menu
    }
    return render(request, 'temporary/contacts.html', context=data)


def forum(request):
    data = {
        'title': 'Форум',
        'menu': menu
    }
    return render(request, 'temporary/forum.html', context=data)
