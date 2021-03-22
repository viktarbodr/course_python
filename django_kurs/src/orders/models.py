from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.contrib.auth import models as auth_models
from cart import models as cart_models
from accounts import models as accs_models

#from accounts import models as ac_models
# Create your models here.

class Orders(models.Model):


    customer = models.ForeignKey(
        accs_models.Customer, 
        verbose_name='Пользоапте', 
        related_name='related_orders', 
        on_delete=CASCADE)

    first_name = models.CharField(
        max_length=40,
        verbose_name='Имя')

    last_name = models.CharField(
        max_length=40, 
        verbose_name='Фамилия')

    phone = models.CharField(
        max_length=22, 
        verbose_name='Телефон')

    cart = models.ForeignKey(
        cart_models.Cart,
        verbose_name='Корзина',
        on_delete=CASCADE,
        null=True,
        blank=True)

    address = models.CharField(
        max_length=100, 
        verbose_name='Адрес', 
        null=True, 
        blank=True)

    purchase_type = models.CharField(
        max_length=80, 
         null=True, 
        blank=True)
        
    comment = models.TextField(
        verbose_name='Комментарий',
        max_length=255,
        null=True, 
        blank=True)

    created_date = models.DateTimeField(
        auto_now=True, 
        verbose_name='Дата создания')

    update_date = models.DateField(
        verbose_name='Дата изменения',
        auto_now=True)

    def __str__(self):
        return f'Заказ n:{self.pk}'

