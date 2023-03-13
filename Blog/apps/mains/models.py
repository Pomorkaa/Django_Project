from django.db import models

# Create your models here.
class Main(models.Model):
    main_title = models.CharField('Заголовок главной страницы', max_length=200)
    main_ipg = models.ImageField('Картинка', null=True, blank=True, upload_to='static/img/')
    main_text = models.TextField('О чем речь вообще, где мы?')  # текст
    pub_date = models.DateTimeField('Дата последнего обновления')


    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'главные страницы'