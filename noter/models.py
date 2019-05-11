from django.db import models

from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, db_index=True, on_delete='Cascade')
    text = models.TextField(verbose_name='Текст заметки', blank=True, default="")
    shorttext = models.CharField(max_length=50, verbose_name='Первые символы', default='Пусто')
    created = models.DateTimeField(verbose_name='Время создания', auto_now_add=True,)
    edited = models.DateTimeField(verbose_name='Последнее изменение', auto_now=True,)
    deleted = models.DateField(verbose_name='Дата удаления', null=True, blank=True)
    locked = models.BooleanField(verbose_name='Только для чтения', default=False)
    protected = models.BooleanField(verbose_name='Запрашивать пароль', default=False)
    color = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Замеки"
        verbose_name = "Заметка"
        ordering = ['-edited']
