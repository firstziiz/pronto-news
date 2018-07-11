# std

# django
from django.test import TestCase

# 3rd

# local
from ..models import Post


# Create your tests here.
class PostTest(TestCase):
    def test_post_should_have_title_and_url(self):
        post = Post.objects.create(
            title='Hello', url='https://www.prontotools.io', number_of_votes=5)
        self.assertEqual(post.title, 'Hello')
        self.assertEqual(post.url, 'https://www.prontotools.io')
        self.assertEqual(post.number_of_votes, 5)
