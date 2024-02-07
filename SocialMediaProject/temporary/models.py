from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse
# python manage.py shell_plus --print-sql


class Forum(models.Model):
    # class Status(models.IntegerChoices):
    #     DRAFT = 0, 'Черновик'
    #     PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Имя статьи')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(blank=True, default=None,
                              null=True, verbose_name='Фотография')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(
        auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug", validators=[
        MinLengthValidator(5, message="Минимум 5 символов"),
        MaxLengthValidator(100, message="Максимум 100 символов"),
    ])

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
