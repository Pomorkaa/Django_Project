from django.db import models
from company.models import Company
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Trip_type(models.Model):
    """Тип экскурсии"""
    type = models.CharField(max_length=500, verbose_name="Тип экскурсии")

    class Meta:
        verbose_name = "Тип экскурсии"
        verbose_name_plural = "Типы экскурсии"
        
    
    def __str__(self):
        return self.type


class Status(models.Model):
    """Статусы для экскурсии"""
    status = models.CharField(max_length=500, verbose_name="Статус загрузки экскурсии")

    class Meta:
        verbose_name = "Статус загрузки экскурсии"
        verbose_name_plural = "Статусы загрузки экскурсии"
        
    
    def __str__(self):
        return self.status

class AdditionalOptions(models.Model):
    """Тэги экскурсий"""

    option = models.CharField(max_length=500, verbose_name="Дополнительная опция")

    class Meta:
        verbose_name = "Дополнительная опция"
        verbose_name_plural = "Дополнительные опции"
        ordering = [
            "option",
        ]

    def __str__(self):
        return self.option


class Trip(models.Model):
    """Сама экскурсия"""
    company = models.ForeignKey(Company, verbose_name = 'Компания', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=500, verbose_name="Название")
    decription = models.TextField(verbose_name='Описание', null=True, blank=True)
    type = models.ForeignKey(Trip_type, verbose_name = 'Тип экскурси', on_delete=models.SET_NULL, null=True)
    number = models.CharField(max_length=50, verbose_name="Транспорт если есть", null=True, blank=True)
    seets= models.IntegerField(verbose_name="Количество мест",null=True, blank=True)
    children_seets=models.BooleanField(default=False, verbose_name="Детские места")
    disabled_seets= models.BooleanField(default=False, verbose_name="Места для инвалидов")
    data = models.DateTimeField(verbose_name='Дата и время начала экскурсии', null=True, blank=True)
    time = models.CharField(max_length=400, verbose_name="Продолжительность экскурсии")
    status = models.ForeignKey(Status, verbose_name = 'Статус', on_delete=models.SET_NULL, null=True)
    details = models.TextField(max_length=500, verbose_name="Дополнительная информация", default=None, null=True, blank=True)
    price = models.IntegerField(verbose_name="Стоимость",null=True,blank=True)
    photo = models.ImageField(verbose_name='Рекламный баннер', upload_to='media/trip')
    stars = models.PositiveIntegerField(
        verbose_name="Количество звёзд", default=0, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    options = models.ManyToManyField(
        AdditionalOptions, verbose_name="Дополнительные опции", related_name="hotels", blank=True
    )



    class Meta:
        verbose_name = "Экскурсия"
        verbose_name_plural = "Экскурсия"     
        ordering = ['name',]
        
        
    
    def __str__(self):
        return self.number

    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return "/static/default.svg"
        
    @property
    def small_image(self):
        name = self.image.name.partition(f"media/trip/{self.title}/")[-1]
        url = self.image.url.replace(name, f"small_{name}")
        return url



class AdditionalImage(models.Model):
    """дополнительные изображения к экскурсии"""

    hotel = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="additionalimages")
    image = models.ImageField(upload_to='media/trip', verbose_name="Изображение")

    class Meta:
        verbose_name_plural = "Еще фото"
        verbose_name = "Еще фото"

    @property
    def small_image(self):
        name = self.image.name.partition(f"meia/trip{self.trip.name}/")[-1]
        url = self.image.url.replace(name, f"small_{name}")
        return url
