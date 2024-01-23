from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from temporary.forms import AddPostForm


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


# def forum(request):
#     data = {
#         'title': 'Форум',
#         'menu': menu
#     }
#     return render(request, 'temporary/forum.html', context=data)

class AddPost(FormView):
    form_class = AddPostForm
    template_name = 'temporary/forum.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
