# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render

from .models import Product

# Create your views here.

def index(request):
    return HttpResponse("Main page of product. Nothing to show here")

def product(request, product_id):
    try:
        obj = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404
    template = loader.get_template('product/product.html')
    context = {
        'product': obj,
    }
    return HttpResponse(template.render(context, request))