from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length=50)
    
    foto = models.ImageField(
        verbose_name='Фото обложки',
        upload_to='uploads/',
        null=True,
        blank=True)
    
    price = models.DecimalField(
        verbose_name='Цена (BYN)',
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        default=0.0)
    
    authors = ManyToManyField(
        'wordbook.Authors',
        verbose_name='Авторы книги',
        blank=True)

    series = ForeignKey(
        'wordbook.Series',
        on_delete = models.PROTECT,
        verbose_name='Серия',
        blank=True,
        null=True)

    genres = ManyToManyField(
        'wordbook.Genres',
        verbose_name='Жанры',
        blank=True)

    year = models.SmallIntegerField(
        verbose_name='Год издания',
        null=True,
        blank=True)

    pages = models.SmallIntegerField(
        verbose_name='Страницы',
        null=True,
        blank=True)

    cover = models.CharField(
        verbose_name='Переплет',
        max_length = 20,
        blank=True,
        null=True)

    forma = models.CharField(
        verbose_name='Формат',
        max_length = 20,
        blank=True,
        null=True)

    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=13,
        blank=True,
        null=True)

    weight = models.SmallIntegerField(
        verbose_name='Вес (гр)',
        null=True,
        blank=True)

    age_stat = models.SmallIntegerField(
        verbose_name='Возрастные ограничения',
        blank=True,
        null=True)

    publisher = ForeignKey(
        'wordbook.Publishers',
        on_delete = models.PROTECT,
        blank=True,
        null=True)

    quantity = models.SmallIntegerField(
        verbose_name='Наличие',
        default=0 )

    active = models.BooleanField(
        verbose_name='Доступен Да/Нет',
        default=True)

    rating = models.IntegerField(
        verbose_name='Рейтинг',
        validators=[MaxValueValidator(10), MinValueValidator(0)],
        null=True,
        blank=True)

    date_create = models.DateTimeField(
        verbose_name='Дата внесения в каталог',
        auto_now_add=True)

    date_update = models.DateTimeField(
        verbose_name='Дата последнего изменения карточки',
        auto_now=True)

    def get_authors(self):
        return "\n".join([p.name for p in self.authors.all()])
    
    def get_genres(self):
        return "\n".join([p.name for p in self.genres.all()])

    def __str__(self):
        return f'{self.pk}, {self.name}'
