from django.urls import path
from . views import *


app_name = 'blogging'
urlpatterns = [
    path("posts/", PostListView.as_view(), name='post_list'),  # نمایش لیست پست‌ها
    path("create_post/", CreatePostView.as_view(), name='create_post'),  #  ایجاد پست
    path("post_detail/<int:pk>/", PostDetailView.as_view(), name='post_detail'),  # نمایش جزئیات یک پست خاص
]



