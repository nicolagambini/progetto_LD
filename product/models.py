# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os, uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    # Fixes bad pluralization
    class Meta:
        verbose_name_plural = 'categories'

def product_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join('img/product', '{}.{}'.format(uuid.uuid4(), ext))

class Product(models.Model):

    # seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=product_image_path, max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class Review(models.Model):

    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    pub_date = models.DateTimeField('date published')