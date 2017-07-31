from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="landing"),

    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),

    url(r'^add-friend/(?P<id>\d+)$', views.addFriend, name='add-friend'),
    url(r'^remove-friend/(?P<id>\d+)$', views.removeFriend, name='remove-friend'),

    url(r'^', views.index, name='default'),
]