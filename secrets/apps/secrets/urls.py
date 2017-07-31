from django.conf.urls import url
from . import views

urlpatterns = [
# load the success page after they haved logged in
    url(r'^$', views.index, name='success'),
# Handlers for POST routes
    url(r'^create$', views.create, name='create_secret'),
    url(r'^like/(?P<id>\d+)$', views.like, name='like_secret'),
# Handlers for routes with peramiters
    url(r'^unlike/(?P<id>\d+)$', views.unlike, name='unlike_secret'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete_secret'),
]