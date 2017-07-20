from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	salt = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Message(models.Model):
	#ForeignKey for a one-to-many relationship. There can be many messages to one User
	user_id = models.ForeignKey(User)
	message = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
	#ForeignKey for a one-to-many relationship. There can be many comments to one message from User
	message_id = models.ForeignKey(Message)
	user_id = models.ForeignKey(User)
	comment = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)