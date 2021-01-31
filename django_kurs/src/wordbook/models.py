from django.db import models

# Create your models here.

class Author(models.Model):
    # pk/id
    author_name = models.CharField(verbose_name = 'Authors name', max_length = 70)
    
    def __str__(self):
       return self.author_name

class Series(models.Model):
    serial = models.CharField(verbose_name ='Book series', max_length = 70)

    def __str__(self):
        return self.serial


class Genre(models.Model):
    genres = models.CharField(verbose_name ='Book genre', max_length = 80)

    def __str__(self):
        return self.genres


class Publish(models.Model):
    publishers = models.CharField(verbose_name='Book publisher', max_length = 80)

    def __str__(self):
        return self.publishers
