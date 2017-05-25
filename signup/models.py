from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings

import os, uuid


# Create your models here.
def seller_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join('img/seller', '{}.{}'.format(uuid.uuid4(), ext))


class User(AbstractUser):
    address = models.CharField(max_length=50)
    sub_date = models.DateTimeField('date subscription')
    tel_number = models.CharField(max_length=20)


class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    iva = models.CharField(validators=[
        RegexValidator(regex='^.{16}$', message='Length has to be 16',
                       code='nomatch')
    ], max_length=11)
    logo = models.ImageField(upload_to=seller_image_path, max_length=100)

    def __str__(self):
        return self.name


# Custom User model
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Customer(models.Model):
    #birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cf = models.CharField(validators=[
        RegexValidator(regex='^.{11}$', message='Length has to be 11',
                       code='nomatch')
    ], max_length=11)