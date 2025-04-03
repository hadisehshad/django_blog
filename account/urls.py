from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'account'
urlpatterns = [
    path('register/', RegisterView.as_view()),  # مسیر ثبت‌نام کاربر جدید
    path('login/', LoginView.as_view()),  # مسیر ورود کاربران
    path('logout/', LogoutView.as_view()),  # مسیر خروج کاربران
    path('password/reset/', PasswordResetView.as_view()),  # درخواست بازنشانی رمز عبور
    path('password/change/', PasswordChangeView.as_view()),  # تغییر رمز عبور با کد تأیید
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # مسیر دریافت refresh و access توکن پس از ورود موفق کاربر
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # مسیر دریافت توکن جدید با استفاده از refresh token برای تمدید access token
]
