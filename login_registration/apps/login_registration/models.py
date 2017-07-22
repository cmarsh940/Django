from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import datetime
import re 
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Skinny models


class UserManager(models.Manager):
    def isValidLogin(self, userInfo):
        loginObject = {
            "errors": []
        }
        validLogin = True
        if User.objects.filter(email = userInfo['email']):
            hashed = User.objects.get(email = userInfo['email']).password
            hashed = hashed.encode('utf-8')
            password = userInfo['password']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                user = User.objects.get(email=userInfo['email'])
                loginObject['user'] = user
            else:
                loginObject['errors'].append("Unsuccessful login, incorrect password")
                validLogin = False
        else:
            loginObject['errors'].append("Unsuccessful login, email is not in database")
            validLogin = False

        return loginObject
                

    def isValidRegistration(self, userInfo):
        registrationObject = {
            "errors": []
        }
        validRegistration = True
        if not userInfo['first_name'].isalpha():
            registrationObject['errors'].append('First name cant have numbers in it')
            validRegistration = False
        if len(userInfo['first_name']) < 1:
            registrationObject['errors'].append('Name cant be empty')
            validRegistration = False
        if not userInfo['last_name'].isalpha():
            registrationObject['errors'].append('Last name cant have numbers in it')
            validRegistration = False
        if len(userInfo['last_name']) < 1:
            registrationObject['errors'].append('Name cant be empty')
            validRegistration = False
        if not EMAIL_REGEX.match(userInfo['email']):
            registrationObject['errors'].append('Not a valid Email')
            validRegistration = False
        if len(userInfo['password']) < 7:
            registrationObject['errors'].append('Password is too short. Must be greater then 8')
            validRegistration = False
        if userInfo['password'] != userInfo['confirm_password']:
            registrationObject['errors'].append('Passwords are not the same')
            validRegistration = False
        if User.objects.filter(email = userInfo['email']):
            registrationObject['errors'].append("This email already exists")
            validRegistration = False

        if validRegistration:
            hashed = bcrypt.hashpw(userInfo['password'].encode(), bcrypt.gensalt())
            new_user = User.objects.create(first_name = userInfo['first_name'], last_name = userInfo['last_name'], email = userInfo['email'], password = hashed)
            registrationObject['user'] = new_user
        return registrationObject

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()