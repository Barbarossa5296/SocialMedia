from django.shortcuts import render
from django.http import HttpResponse


menu = [
    {'title': 'Главная'},
    {'title': 'Товарищи'},
    {'title': 'Сообщения'},
    {'title': 'Форум'},
    {'title': 'Контакты'},
]


def index(request):
    return render(request, 'temporary/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'temporary/about.html', {'title': 'Контакты'})


def messages(request):
    return render(request, 'temporary/messages.html', {'title': 'Сообщения'})


def comrades(request):
    return render(request, 'temporary/friends.html', {'title': 'Товарищи'})


def forum(request):
    return render(request, 'temporary/forum.html', {'title': 'Форум'})
