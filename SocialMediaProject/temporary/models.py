from django.db import models


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
