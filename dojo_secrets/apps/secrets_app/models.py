from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User

class SecretManager(models.Manager):
    def createSecret(self, form_data, user):
        secret = Secret.objects.create(
            content = form_data['content'],
            user = user,
        )

        return secret

class Secret(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name="secrets")
    liked_by = models.ManyToManyField(User, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SecretManager()
