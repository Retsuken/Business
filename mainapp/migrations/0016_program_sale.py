# Generated by Django 4.2 on 2024-03-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_program_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='sale',
            field=models.IntegerField(blank=True, null=True, verbose_name='Стоймость обучение скидка'),
        ),
    ]
