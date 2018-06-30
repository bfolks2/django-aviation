from django.shortcuts import render, get_object_or_404

from prepair.views import PrepairViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(PrepairViewSet):
    """
    DRF Viewset for Post objects
    """

    DB_MODEL_CLASS = Post
    SERIALIZER_CLASS = PostSerializer


class CommentViewSet(PrepairViewSet):
    """
    DRF Viewset for Comment objects
    """

    DB_MODEL_CLASS = Comment
    SERIALIZER_CLASS = CommentSerializer
