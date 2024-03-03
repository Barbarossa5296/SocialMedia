from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from .models import Comment
from .forms import CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from temporary.models import Forum


class AddComment(LoginRequiredMixin, FormView):
    template_name = 'temporary/post.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Forum, slug=self.kwargs['slug'])
        context['post'] = post
        context['form'] = CommentForm()
        return context

    def form_valid(self, form):
        post = get_object_or_404(Forum, slug=self.kwargs['slug'])
        comment = form.save(commit=False)
        comment.post = post
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = get_object_or_404(Forum, slug=self.kwargs['slug'])
        return reverse_lazy('post', kwargs={'slug': post.slug})
