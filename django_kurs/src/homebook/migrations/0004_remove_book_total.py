# Generated by Django 3.1.6 on 2021-03-21 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homebook', '0003_book_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='total',
        ),
    ]
