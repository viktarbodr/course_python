# Generated by Django 3.1.6 on 2021-03-21 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20210321_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartproduct',
            old_name='book',
            new_name='c_book',
        ),
        migrations.RenameField(
            model_name='cartproduct',
            old_name='cart',
            new_name='c_cart',
        ),
    ]
