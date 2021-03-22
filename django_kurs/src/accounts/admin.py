from django.contrib import admin
from accounts import models
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Customer._meta.get_fields()]

admin.site.register(models.Customer, CustomerAdmin)
