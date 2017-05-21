from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<product_id>[0-9]+)/', views.product, name='product'),
    url(r'^$', views.index, name='index'),
]