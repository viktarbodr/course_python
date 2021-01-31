from django.contrib import admin

# Register your models here.
from .models import Author, Series, Genre, Publish

admin.site.register(Author)
admin.site.register(Series)
admin.site.register(Genre)
admin.site.register(Publish)