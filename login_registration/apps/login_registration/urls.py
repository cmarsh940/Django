from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register_page$', views.register_page, name='register_page'),
	url(r'^login_page$', views.login_page, name='login_page'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.login, name='logout'),
    url(r'^success$', views.success, name='success'),
]