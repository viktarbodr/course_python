# Generated by Django 3.1.6 on 2021-03-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homebook', '0002_auto_20210320_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.SmallIntegerField(default=0, verbose_name='Наличие'),
        ),
    ]
