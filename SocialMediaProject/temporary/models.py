from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse
from django.conf import settings
from transliterate import translit


class Forum(models.Model):

    title = models.CharField(max_length=255, verbose_name='Имя статьи')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(blank=True, default=None,
                              null=True, verbose_name='Фотография')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(
        auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug", validators=[
        MinLengthValidator(5, message="Минимум 5 символов"),
        MaxLengthValidator(100, message="Максимум 100 символов"),
    ], blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='forum_posts')

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # autoslug for title, if title change, slug change too
        if self.title:
            self.slug = translit(self.title, 'ru', reversed=True).lower()
        # validate user for auth before add
        if not self.author_id and kwargs.get('user') and kwargs['user'].is_authenticated:
            self.author = kwargs['user']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
