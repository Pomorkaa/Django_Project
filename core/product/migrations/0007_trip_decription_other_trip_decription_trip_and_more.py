# Generated by Django 4.1.6 on 2023-08-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_trip_decription'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='decription_other',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительная информация'),
        ),
        migrations.AddField(
            model_name='trip',
            name='decription_trip',
            field=models.TextField(blank=True, null=True, verbose_name='Детали поездки'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='decription',
            field=models.TextField(blank=True, null=True, verbose_name='Описание машрута'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='details',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='Короткий баннер для сайта'),
        ),
    ]
