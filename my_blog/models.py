from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField('Оглавление', max_length=255)
    text = models.TextField('Статья')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def edit_url(self):
        return reverse('edit', args=(self.pk, ))