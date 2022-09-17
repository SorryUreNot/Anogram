from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from posts.models import post
from posts.serializers import PostsSerializer


class PostViewSet(ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostsSerializer


