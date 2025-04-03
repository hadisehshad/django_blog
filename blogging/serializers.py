from rest_framework import serializers
from .models import *
from account.models import User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["title", "content", "image", "author"]

    def get_author(self, obj):
        return obj.author.username
