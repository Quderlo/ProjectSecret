from django.db import models
from django.urls import reverse

class Task(models.Model):
    title = models.CharField('Название задания', max_length=200)
    file = models.FileField('Архив', upload_to='tasks/', blank=True, null=True)
    external_url = models.URLField('Ссылка на сайт', blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task-download', args=[str(self.id)])