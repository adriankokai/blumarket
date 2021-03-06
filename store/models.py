from django.db import models
import os
import uuid

# Create your models here.
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = filename + str(uuid.uuid4()) + ext
    return os.path.join('static/product_images/', filename)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    stock = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to=content_file_name)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="product_images", on_delete=models.CASCADE)
    photo = models.FileField(upload_to=content_file_name)

    def __str__(self):
        return self.product.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='warehouse')
    customer_address = models.TextField()
    customer_city = models.CharField(max_length=255)
    customer_postal_code = models.CharField(max_length=255)
    customer_region = models.CharField(max_length=255)
    customer_name  = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    customer_email = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + ' ' + str(self.product.name) + ' ' + str(self.customer_name)

class Txn(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.CharField(max_length=255)

    def __str__(self):
        return self.order
