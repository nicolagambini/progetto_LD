# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Product

# Create your views here.

def index(request):
    return HttpResponse("Main page of product. Nothing to show here")

class ProductView(generic.DetailView):
    model = Product
    template_name = 'product/product.html'