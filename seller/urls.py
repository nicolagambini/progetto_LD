from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<seller_id>[0-9]+)/', views.seller, name='seller'),
]