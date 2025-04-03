from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError

from .models import *


# Validators
def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin cant be in email')


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'validators': (clean_email,)}
        }

    # Object-level validation
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords must match')
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(write_only=True, required=True)


class PasswordResetSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, required=True)

    def validate_phone_number(self, value):
        """
               بررسی می‌کند که شماره تلفن در سیستم ثبت شده باشد.
        """
        if not User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("شماره تلفن یافت نشد. لطفاً شماره صحیح وارد کنید.")
        return value


class ChangePasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, required=True)
    reset_code = serializers.CharField(max_length=6, required=True)
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        """
          بررسی می‌کند که کد تأیید معتبر باشد و رمز عبور جدید قوی باشد.
        """
        phone_number = data.get("phone_number")
        reset_code = data.get("reset_code")
        new_password = data.get("new_password")

        # بررسی وجود کاربر
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise serializers.ValidationError({"phone_number": "شماره تلفن معتبر نیست."})

        # بررسی درخواست بازنشانی رمز عبور
        try:
            reset_request = PasswordResetRequest.objects.get(user=user, reset_code=reset_code)
        except PasswordResetRequest.DoesNotExist:
            raise serializers.ValidationError({"reset_code": "کد تایید نادرست است."})

        # بررسی انقضای کد تأیید
        if reset_request.is_expired():
            raise serializers.ValidationError({"reset_code": "کد تایید منقضی شده است."})

        # بررسی پیچیدگی رمز عبور
        try:
            validate_password(new_password, user)
        except ValidationError as e:
            error_messages = e.messages if hasattr(e, "messages") else e.args[0]
            raise serializers.ValidationError({"new_password": error_messages})

        return data
