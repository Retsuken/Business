# Generated by Django 4.2 on 2024-04-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0046_program_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo_image', verbose_name='Логотипы'),
        ),
    ]
