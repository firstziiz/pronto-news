from django.test import TestCase
from ..models import Post
from ..forms import PostForm


class PostFormTest(TestCase):
    def test_from_should_use_post_model(self):
        self.assertEqual(PostForm.Meta.model, Post)
