from django.contrib import admin
from homebook import models as homebook_models
# Register your models here.


class HomeBookAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 
        'name',
        'foto',
        'price',
        'get_authors',
        'series',
        'get_genres',
        'year',
        'pages',
        'cover',
        'forma',
        'isbn',
        'weight',
        'age_stat',
        'publisher',
        'quantity',
        'active',
        'rating',
        'date_create',
        'date_update'
    ]

admin.site.register(homebook_models.Book, HomeBookAdmin)