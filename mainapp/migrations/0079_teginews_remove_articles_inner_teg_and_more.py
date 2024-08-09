# Generated by Django 4.2 on 2024-05-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0078_alter_articles_inner_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='TegiNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teg', models.TextField(verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Теги (статьи)',
                'verbose_name_plural': 'Теги (статьи)',
            },
        ),
        migrations.RemoveField(
            model_name='articles_inner',
            name='teg',
        ),
        migrations.AddField(
            model_name='articles_inner',
            name='teg',
            field=models.ManyToManyField(to='mainapp.teginews', verbose_name='Теги'),
        ),
    ]
