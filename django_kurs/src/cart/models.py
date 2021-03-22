from django.db import models 
from django.db.models.deletion import CASCADE, PROTECT
from django.contrib.auth import get_user_model
#from accounts  import models 
from homebook  import models as home_models
from accounts  import models as accs_models
# Create your models here.

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User, 
        verbose_name='Покупатель',
        on_delete=PROTECT,
        related_name='cart',
        blank=False,
        null=True)

    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True)

    update_date = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True)

    def __str__(self):
        return f"Корзина #{self.pk}"

    @property
    def total_book_price(self):
        total = 0
        for book in self.book.all():
            total += book.total_price
        return total
        



class CartProduct(models.Model):

    cart = models.ForeignKey(
        Cart, 
        verbose_name='Корзина', 
        on_delete=CASCADE, 
        related_name='books_cart',
        blank=False,
        null=True)

    book = models.ForeignKey(
        home_models.Book, 
        verbose_name='Книга в корзине',
        on_delete=PROTECT,
        related_name='book_in_cart')

    quantity = models.IntegerField(default=1)

    price = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        verbose_name='Общая стоимость')

    def __str(self):
        return f"В Корзине: #{self.book} quantity {self.quantity} price{self.price}"  
    


    @property
    def total_price(self, *args, **kwargs):
        return self.book.price * self.quantity  


    
