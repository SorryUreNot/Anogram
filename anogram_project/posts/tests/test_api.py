from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from posts.models import post
from posts.serializers import PostsSerializer


class PostsApiTestCase(APITestCase):
    def test_get(self):
        post1 = post.objects.create(text='Бэйл руинер', likes=778)
        post2 = post.objects.create(text='судья пидрас', likes=5999)

        url = reverse('post-list')
        #print(url)
        response = self.client.get(url)
        serializer_data = PostsSerializer([post1, post2], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

        #print(response.data)
