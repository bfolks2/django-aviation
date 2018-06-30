from rest_framework.serializers import ModelSerializer
from .models import Post, Comment


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('member', 'airport', 'body', 'datetime_created', 'datetime_updated')


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('member', 'post', 'body', 'datetime_created', 'datetime_updated')
