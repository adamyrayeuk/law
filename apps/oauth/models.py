from django.db import models
from django.conf import settings

class OAuth(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    refresh_token = models.CharField(unique=True, max_length=40, blank=True, null=True)
    access_token = models.CharField(unique=True, max_length=40, blank=True, null=True)
    expired_datetime = models.DateTimeField(auto_now=True)