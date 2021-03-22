from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE, PROTECT

# Create your models here.
User = get_user_model() 

class Customer(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name='Пользоаптель', 
        on_delete=CASCADE)

    phone = models.CharField(
        max_length=22, 
        verbose_name='Телефон', 
        null=True, 
        blank=True)

    city = models.CharField(
        verbose_name='Город',
        max_length=80,
        null=True, 
        blank=True,)

    address = models.CharField(
        max_length=80, 
        verbose_name='Адрес', 
        null=True, 
        blank=True)

    index = models.CharField(
        verbose_name='Почтовый индекс',
        max_length=80,
        blank=True,
        null=True)

    def __str__(self):
        return f'{self.phone}, {self.city}, {self.address}, {self.index}'


