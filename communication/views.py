from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(ViewSet):
    """
    DRF Viewset for Post objects
    """

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class CommentViewSet(ViewSet):
    """
    DRF Viewset for Comment objects
    """

    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
