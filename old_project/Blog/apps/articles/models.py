from django.db import models

# Create your models here.


#python manage.py makemigrations articles  сделать миграцию после внесения данных в сеттинг
#python manage.py sqlmigrate 0001 - покажет что создал на sql языке
#python manage.py migrate - все миграции сразу если вылетает ошибка
#мета информация чтоб переименовать столбцы


#конфигурационная модель класса
class Article(models.Model):
    article_title = models.CharField('Заголовок статьи', max_length=200) #как варчар то же самое
    article_text = models.TextField('Текст статьи')                         #текст
    pub_date = models.DateTimeField('Дата публикации')                      #в sql будет дата

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'