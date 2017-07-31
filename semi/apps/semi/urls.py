from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'), 
    url(r'^product/$', views.product, name='product'), 
    url(r'^product/new$', views.add_product, name='add_product'), 
    url(r'^product/handle_add_product$', views.handle_add_product, name='handle_add_product'), 
]