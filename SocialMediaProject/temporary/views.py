from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from .models import Forum
from rest_framework import viewsets
from .serializers import ForumSerializer
from temporary.forms import AddPostForm


class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer


class HomePage(ListView):
    template_name = 'temporary/index.html'
    model = Forum

    def get_queryset(self):
        return Forum.objects.filter(is_published=True)


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


class AddPost(CreateView):
    model = Forum
    form_class = AddPostForm
    template_name = 'temporary/add_post.html'


class EditPost(UpdateView):
    model = Forum
    form_class = AddPostForm
    template_name = 'temporary/add_post.html'


class ShowPost(DetailView):
    model = Forum
    template_name = 'temporary/post.html'
    context_object_name = 'post'
