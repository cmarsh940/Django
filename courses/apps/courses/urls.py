from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses$', views.courses, name='courses'),
    url(r'^course_delete/(?P<id>\d+)$', views.course_delete),
]