from django.db import models

# Create your models here.


class Authors(models.Model):
    # pk/id
    name = models.CharField(
        verbose_name='Author name', 
        max_length=40)
    description = models.TextField(
        verbose_name= "Description_name",
        null=True,
        blank=True)

    def __str__(self):
       return self.name

class Series(models.Model):
    name = models.CharField(
        verbose_name='Book series', 
        max_length=40)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(
        verbose_name='Book genre', 
        max_length=70)
    
    def __str__(self):
        return self.name


class Publishers(models.Model):
    name = models.CharField(
        verbose_name='Book publisher',
         max_length=70)

    def __str__(self):
        return self.name
