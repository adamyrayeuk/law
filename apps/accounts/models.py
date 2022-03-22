from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 

import random
import string

class AccountManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The username must be set')
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):  
        """  
        Create and save a SuperUser with the given email and password.  
        """  
        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)  
        extra_fields.setdefault('is_active', True)  
  
        if extra_fields.get('is_staff') is not True:  
            raise ValueError(_('Superuser must have is_staff=True.'))  
        if extra_fields.get('is_superuser') is not True:  
            raise ValueError(_('Superuser must have is_superuser=True.'))  
        return self.create_user(username, password, **extra_fields)  


class Account(AbstractBaseUser, PermissionsMixin):
    email = None
    username = models.CharField(unique=True, max_length=255)
    fullname = models.CharField(max_length=255)
    npm = models.CharField(unique=True, max_length=10)
    client_id = models.CharField(unique=True, max_length=16)
    client_secret = models.CharField(unique=True, max_length=32)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['npm', 'fullname']

    objects = AccountManager()

    def __str__(self):
        return self.username