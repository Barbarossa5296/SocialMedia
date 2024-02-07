from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from .models import Forum

from temporary.forms import AddPostForm


class HomePage(ListView):
    template_name = 'temporary/index.html'
    model = Forum


class About(TemplateView):
    template_name = 'temporary/about.html'


def messages(request):
    data = {
        'title': 'Сообщения',
    }
    return render(request, 'temporary/messages.html', context=data)


@login_required(login_url='users:login')  # переделать в класс
def contacts(request):
    data = {
        'title': 'Контакты',
    }
    return render(request, 'temporary/contacts.html', context=data)


class AddPost(FormView):
    form_class = AddPostForm
    template_name = 'temporary/forum.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ShowPost(DetailView):
    model = Forum
    template_name = 'temporary/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
