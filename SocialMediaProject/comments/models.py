from django.db import models
from django.conf import settings
from temporary.models import Forum


class Comment(models.Model):
    post = models.ForeignKey(
        Forum, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.author.username} - {self.created}'
