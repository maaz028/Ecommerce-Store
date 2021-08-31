from django.contrib import admin

# Register your models here.

from .models import Product, contact, order, update_order

admin.site.register(Product)

admin.site.register(contact)
admin.site.register(order)
admin.site.register(update_order)