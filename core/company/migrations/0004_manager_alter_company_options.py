# Generated by Django 4.1.6 on 2023-08-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_company_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(max_length=400, verbose_name='ФИО Менеджера')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Короткое описание менеджера')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
    ]
