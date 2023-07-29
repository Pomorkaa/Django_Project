from django.db import models

# Create your models here.
from django.db import models
from datetime import date
import employees.models as employ


# Create your models here.
class Wiki(models.Model):

    wiki_name = models.CharField('Тема инструкции', max_length=200)
    wiki_date = models.DateField('Дата последнего редактирования', default=date.today, )
    wiki_autor = models.CharField('Автор инструкции', choices=employ.employees.PROFESSION, max_length=200)
    wiki_url = models.URLField('Ссылка на документацию')

    def __str__(self):
        return self.wiki_name

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'
