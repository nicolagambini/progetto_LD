from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Seller


# Create your views here.
def seller(request, seller_id):
    obj = get_object_or_404(Seller, pk=seller_id)
    context = {
        'seller' : obj
    }
    return render(request, 'seller/seller.html', context)