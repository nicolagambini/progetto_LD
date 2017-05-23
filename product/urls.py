from django.conf.urls import url

from . import views

app_name = 'products'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/', views.ProductView.as_view(), name='product'),
    url(r'^$', views.index, name='index'),
]