from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
