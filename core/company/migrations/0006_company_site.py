# Generated by Django 4.1.6 on 2023-08-02 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_manager_prof'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='site',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на сайт'),
        ),
    ]
