# Generated by Django 3.2.12 on 2022-02-17 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='is_available'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default=None, max_length=255, verbose_name='Title'),
        ),
    ]
