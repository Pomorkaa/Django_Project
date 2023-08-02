from django.db import models

# Create your models here.
class Company(models.Model):
    """Компания"""
    name = models.CharField(max_length=400,verbose_name='Название компании' )
    manager = models.CharField(max_length=400,verbose_name='ФИО Менеджера' )
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    photo = models.ImageField(blank=True,null=True)
    short_description = models.TextField(verbose_name='Короткое описание менеджера', blank=True, null=True)
    site = models.URLField(verbose_name='Ссылка на сайт', blank=True ,null=True)
    referal = models.BooleanField(verbose_name='Партнер в бонусной системе', default=False)
    requisites = models.FileField(verbose_name='Реквизиты', blank=True, null=True)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name

class Manager(models.Model):
    """Менеджеры и сотрудники"""
    manager = models.CharField(max_length=400,verbose_name='ФИО Менеджера' )
    phone = models.CharField(max_length=50, verbose_name="Телефон", blank=True, null=True)
    prof= models.CharField(max_length=50, verbose_name="Должность", blank=True, null=True)
    photo = models.ImageField(blank=True,null=True)
    short_description = models.TextField(verbose_name='Короткое описание менеджера', blank=True, null=True)


    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.manager
    

class Document(models.Model):
    """Модель для подгрузки соглашений и документов"""
    title = models.CharField(verbose_name="Название документа", max_length=200)
    file = models.FileField(upload_to='document/' , verbose_name="Файл",)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
        
        
class Contacts(models.Model):
    """Модель для подгрузки соглашений и документов"""
    name = models.CharField(verbose_name="Название", max_length=200)
    adress = models.CharField(verbose_name="Адрес", max_length=200)
    phone = models.CharField(verbose_name="Телефон", max_length=200)
    whatsapp = models.CharField(verbose_name="Вотсапп", max_length=200)
    tg = models.CharField(verbose_name="Телеграмм", max_length=200)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"