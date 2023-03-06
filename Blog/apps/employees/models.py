from django.db import models


# Create your models here.

class employees(models.Model):
    junior ='Стажеришка'
    gendir ='Товарищ Генеральный директор'
    buxgalt = 'батюшка бухгалтер'
    ispdir = 'исполнительный директоришка'
    PROFESSION = [(gendir, 'Генеральный директор'),
        (buxgalt, 'Бухгалтер'),
        (ispdir, 'Исполнительный директор'),
        (junior, 'Стажер')]
    employees_name = models.CharField('ФИО', max_length=200) #как варчар то же самое
    employees_birthday = models.DateField('Дата рождения', null=True, blank=True)               #может быть ноль значение
    employees_prof = models.CharField('Должность', max_length=30, choices=PROFESSION, default=junior)
    def __str__(self):
        return self.employees_name
    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'Сотрудники'

