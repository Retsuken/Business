# Generated by Django 4.2 on 2024-04-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0040_remove_program_obuch1_remove_program_obuch2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obuch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obuch', models.TextField()),
            ],
            options={
                'verbose_name': 'Кому подойдет обучение',
                'verbose_name_plural': 'Кому подойдет обучение',
            },
        ),
        migrations.AlterField(
            model_name='program_sod',
            name='sod',
            field=models.TextField(verbose_name='Содержание'),
        ),
    ]
