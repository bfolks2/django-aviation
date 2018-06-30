from django.shortcuts import render, get_object_or_404

from prepair.views import PrepairViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(PrepairViewSet):
    """
    DRF Viewset for Post objects
    """

    prepair_model_class = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_fields = ('pk', 'member', 'airport')
    iexact_filter_fields = tuple()


class CommentViewSet(PrepairViewSet):
    """
    DRF Viewset for Comment objects
    """

    prepair_model_class = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    filter_fields = ('pk', 'member', 'post')
    iexact_filter_fields = tuple()
