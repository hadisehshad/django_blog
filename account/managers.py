from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, phone_number, password=None, **extra_fields):
        if not username:
            raise ValueError('the username field must be set')
        if not email:
            raise ValueError('the email field must be set')
        if not phone_number:
            raise ValueError('The Phone number field must be set')
        if not password:
            raise ValueError('the password field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(username=username, email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True.')
        return self.create_user(username, email, phone_number, password, **extra_fields)
