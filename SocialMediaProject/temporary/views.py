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
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden


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


class AddPost(CreateView):
    model = Forum
    form_class = AddPostForm
    template_name = 'temporary/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(UserPassesTestMixin, UpdateView):
    model = Forum
    form_class = AddPostForm
    template_name = 'temporary/add_post.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'slug': self.object.slug})

    def handle_no_permission(self):
        return HttpResponseForbidden('У вас нет прав на редактирование этого поста.')


class ShowPost(DetailView):
    model = Forum
    template_name = 'temporary/post.html'
    context_object_name = 'post'


class MyPosts(ListView):
    template_name = 'temporary/my_posts.html'
    model = Forum

    def get_queryset(self):
        author = self.request.user
        return Forum.objects.filter(author=author)


class DeletePost(DeleteView):
    model = Forum
    success_url = reverse_lazy('my_posts')
    template_name = 'temporary/my_posts.html'
