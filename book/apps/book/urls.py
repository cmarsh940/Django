from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='books'),
    url(r'^add$', views.add_book, name='add_book'),
    url(r'^handle_add_book$', views.handle_add_book, name='handle_add_book'),
    url(r'^books/(?P<book_id>\d+)$', views.show_book, name='show_book'),
    url(r'^books/(?P<book_id>\d+)/add_review', views.handle_add_review, name='handle_add_review'),
    url(r'^users/(?P<user_id>\d+)$', views.show_user, name='show_user'),
    # url(r'^reviews/delete/(?P<review_id>\d+)$', views.delete_review, name='delete_review'),
]