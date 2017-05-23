# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 07:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('iva', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 11', regex='^.{11}$')])),
                ('address', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='img/product/')),
                ('pub_date', models.DateTimeField(verbose_name='date subscription')),
            ],
        ),
        migrations.AddField(
            model_name='reviewseller',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller'),
        ),
    ]