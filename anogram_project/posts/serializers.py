from rest_framework.serializers import ModelSerializer

from posts.models import post


class PostsSerializer(ModelSerializer):
    class Meta:
        model = post
        fields = ('id', 'text', 'likes')
