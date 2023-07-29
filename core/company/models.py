from django.db import models

# Create your models here.
class Company(models.Model):
    """Компания"""
    name = models.CharField(max_length=400,verbose_name='Название компании' )
    manager = models.CharField(max_length=400,verbose_name='ФИО Менеджера' )
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    referal = models.BooleanField(verbose_name='Партнер в бонусной системе', default=False)
    requisites = models.FileField(verbose_name='Реквизиты', blank=True, null=True)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компания"

    def __str__(self):
        return self.name

