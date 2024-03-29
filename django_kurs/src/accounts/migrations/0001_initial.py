# Generated by Django 3.1.6 on 2021-03-20 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=22, null=True, verbose_name='Телефон')),
                ('city', models.CharField(blank=True, max_length=80, null=True, verbose_name='Город')),
                ('address', models.CharField(blank=True, max_length=80, null=True, verbose_name='Адрес')),
                ('index', models.CharField(blank=True, max_length=80, null=True, verbose_name='Почтовый индекс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользоаптель')),
            ],
        ),
    ]
