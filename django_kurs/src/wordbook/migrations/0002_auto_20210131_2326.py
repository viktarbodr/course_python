# Generated by Django 3.1.5 on 2021-01-31 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='author_name',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='name',
            new_name='genres',
        ),
        migrations.RenameField(
            model_name='publish',
            old_name='name',
            new_name='publishers',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='name',
            new_name='serial',
        ),
    ]