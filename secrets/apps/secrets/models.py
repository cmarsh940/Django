from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
from django.db import models
import re 
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class userManager(models.Manager):
	def validRegistration(self, form_data):
		errors = []
		
		
		if len(form_data['first_name']) == 0:
			errors.append("First Name is required.")
		if len(form_data['last_name']) == 0:
			errors.append("Last Name is required.")
		if len(form_data['email']) == 0:
			errors.append("Email is required.")
		if len(form_data['password']) == 0:
			errors.append("Password is required.")
		if form_data['password'] != form_data['confirm_password']:
			errors.append("Passwords do not match.")

		return errors

	def validLogin(self, form_data):
		errors = []

		user = User.objects.filter(email = form_data['email']).first()

		if len(form_data['email']) == 0:
			errors.append("Email is required.")
		if len(form_data['password']) == 0:
			errors.append("Password is required.")
		if user == []
			errors.append('Accounts does not exit. Please register.')

		return errors

	def createUser(self, form_data):
		password = str(form_data['password'])
		hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

		user = User.objects.create(
			first_name = form_data['first_name'],
			last_name = form_data['last_name'],
			email = form_data['email'],
			password = hashed_pw,
			)
		return user

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
	objects = userManager()