from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.messages.context_processors import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, PasswordResetSerializer, ChangePasswordSerializer
from utils import send_sms
from django.contrib.auth.hashers import make_password


class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        ser_data = RegisterSerializer(data=request.data)
        if ser_data.is_valid():
            validated_data = ser_data.validated_data
            validated_data.pop('password2')
            user = User(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):


    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        ser_data = LoginSerializer(data=request.data)

        if ser_data.is_valid():
            email = ser_data.validated_data['email']
            password = ser_data.validated_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                request.session['access_token'] = access_token
                request.session['refresh_token'] = refresh_token
                return Response({
                    'message': 'Login successful',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }, status=status.HTTP_200_OK)

            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.session.pop('access_token', None)
            request.session.pop('refresh_token', None)

            # دریافت و حذف refresh_token از کاربر
            refresh_token = request.data.get("refresh_token")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

            return Response({"message": "با موفقیت از حساب کاربری خارج شدید."}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data["phone_number"]
            user = User.objects.get(phone_number=phone_number)

            reset_code = PasswordResetRequest.generate_reset_code()
            PasswordResetRequest.objects.create(user=user, reset_code=reset_code)

            send_sms(user.phone_number, reset_code)
            return Response({"messages": "کد تایید ارسال شد."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data["phone_number"]
            reset_code = serializer.validated_data["reset_code"]
            new_password = serializer.validated_data["new_password"]

            user = User.objects.get(phone_number=phone_number)
            reset_request = PasswordResetRequest.objects.get(user=user, reset_code=reset_code)

            if reset_request.is_expired():
                return Response({"reset_code": "کد تایید منقضی شده است."}, status=status.HTTP_400_BAD_REQUEST)

            user.password = make_password(new_password)
            user.save()
            reset_request.delete()

            return Response({"message": "رمز عبور با موفقیت تغییر کرد."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
