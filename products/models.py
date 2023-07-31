from django.db import models

# Create your models here.


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    discount = models.FloatField()


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)