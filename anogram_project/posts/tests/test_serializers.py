from unittest import TestCase

from posts.models import post
from posts.serializers import PostsSerializer


class PostSerializerTestCase(TestCase):
    def test_ok(self):
        post1 = post.objects.create(text='Бэйл руинер', likes=778)
        post2 = post.objects.create(text='судья пидрас', likes=5999)
        data = PostsSerializer([post1, post2], many=True).data
        expected_data = [
            {
                'id': post1.id,
                'text': 'Бэйл руинер',
                'likes': 778
            },
            {
                'id': post2.id,
                'text': 'судья пидрас',
                'likes': 5999
            },
        ]
        #print(data)

        self.assertEqual(expected_data, data)
