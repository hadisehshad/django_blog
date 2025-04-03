from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
import random
from django.utils import timezone
from datetime import timedelta
from utils import send_sms


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self):
        return f"{self.username} - {self.email} - {self.phone_number}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


def get_expiry_time():
    return timezone.now() + timedelta(minutes=20)


class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_reset_requests')
    reset_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=get_expiry_time)

    def __str__(self):
        return f"Password Reset Request for {self.user.username}"

    def is_expired(self):
        return timezone.now() > self.expires_at

    @staticmethod
    def generate_reset_code():
        return str(random.randint(100000, 999999))

    def send_reset_code(self):
        send_sms(self.user.phone_number, self.reset_code)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.send_reset_code()
