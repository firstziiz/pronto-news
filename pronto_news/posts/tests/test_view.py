from django.test import TestCase
from django.urls import reverse

from ..models import Post


class PostListViewTest(TestCase):
    # def test_post_list_view_should_xxx(self):
    # self.assertTrue(False)

    def test_post_list_view_should_be_accessible(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    # Given
    # When
    # Then
    def test_post_list_view_should_show_list_of_post(self):
        Post.objects.create(title='Hello world1', url='http://hello1.world.me')
        Post.objects.create(title='Hello world2', url='http://hello2.world.me')

        response = self.client.get(reverse('post_list'))

        expected = '<li><a href="http://hello1.world.me">Hello world1</a></li>'
        self.assertContains(response, expected, status_code=200)

        expected = '<li><a href="http://hello2.world.me">Hello world2</a></li>'
        self.assertContains(response, expected, status_code=200)