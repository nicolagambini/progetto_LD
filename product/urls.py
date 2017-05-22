from django.conf.urls import url

from . import views

# Resolves naming conflicts. Example:
#   <a href="{% url 'detail' product.id %}">...</a>
# becomes
#   <a href="{% url 'products:detail' product.id %}">...</a>
# since there could be more than one 'detail' url in the same project (for
# example, in different apps)
app_name = 'products'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/', views.ProductView.as_view(), name='product'),
    url(r'^$', views.index, name='index'),
]