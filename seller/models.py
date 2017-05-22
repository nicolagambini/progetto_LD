# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=50)
    iva = models.CharField(validators=[
        RegexValidator(regex='^.{11}$', message='Length has to be 11', code='nomatch')
    ], max_length=11)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/product/', max_length=100)
    pub_date = models.DateTimeField('date subscription')

    def __str__(self):
        return self.name


class Feedback(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    pub_date = models.DateTimeField('date published')
