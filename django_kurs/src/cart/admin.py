from django.contrib import admin

# Register your models here.
from cart import models


class CartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Cart._meta.fields]


class CartProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.CartProduct._meta.fields]


admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartProduct, CartProductAdmin)