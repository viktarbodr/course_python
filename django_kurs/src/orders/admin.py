from django.contrib import admin
from orders import models

# Register your models here.

class OrdersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Orders._meta.fields]


admin.site.register(models.Orders, OrdersAdmin)