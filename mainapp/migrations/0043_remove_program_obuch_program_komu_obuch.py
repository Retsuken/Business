# Generated by Django 4.2 on 2024-04-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0042_obuch_opis_alter_obuch_obuch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='obuch',
        ),
        migrations.AddField(
            model_name='program',
            name='komu_obuch',
            field=models.ManyToManyField(to='mainapp.obuch'),
        ),
    ]
