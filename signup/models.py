from django.db import models
from django.core.validators import RegexValidator

import os, uuid

# Create your models here.

def seller_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join('img/seller', '{}.{}'.format(uuid.uuid4(), ext))

class Seller(models.Model):
    name = models.CharField(max_length=50)
    iva = models.CharField(validators=[
        RegexValidator(regex='^.{11}$', message='Length has to be 11',
                       code='nomatch')
    ], max_length=11)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to=seller_image_path, max_length=100)
    sub_date = models.DateTimeField('date subscription')

    def __str__(self):
        return self.name