from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    img = models.ImageField('Изображение')
    full_text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
