from django.contrib import admin

# Register your models here.
from .models import Authors, Series, Genres, Publishers

class AuthorsAdmin(admin.ModelAdmin):
   #search_fields = ['name']
   list_display = ['pk', 'name', 'description']

class SeriesAdmin(admin.ModelAdmin):
   list_display = ['pk', 'name']

class GenresAdmin(admin.ModelAdmin):
   list_display = ['pk', 'name']

class PublishersAdmin(admin.ModelAdmin):
   list_display = ['pk', 'name',]
      
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Series,SeriesAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Publishers, PublishersAdmin)