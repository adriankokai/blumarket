from django.contrib import admin
from .models import Product, ProductImage, Order, Txn

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(Txn)