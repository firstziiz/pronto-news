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

    def test_post_list_view_should_have_post_form(self):
        response = self.client.get(reverse('post_list'))

        expected = '<form action="." method="post">'
        self.assertContains(response, expected, status_code=200)

        expected = "<input type='hidden' name='csrfmiddlewaretoken'"
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="text" name="title" maxlength="160" required id="id_title" />'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="url" name="url" maxlength="200" required id="id_url" />'
        self.assertContains(response, expected, status_code=200)

        expected = '<button type="submit">'
        self.assertContains(response, expected, status_code=200)

    def test_post_list_view_should_save_data_when_post_data(self):
        data = {
            'title': 'Haloooooo ~',
            'url': 'https://www.prontomarketing.com'
        }
        response = self.client.post(
            reverse('post_list'), data=data, follow=True)

        expected = '<li><a href="https://www.prontomarketing.com">Haloooooo ~</a></li>'
        self.assertContains(response, expected, status_code=200)

        post = Post.objects.last()

        self.assertEqual(post.title, 'Haloooooo ~')
        self.assertEqual(post.url, 'https://www.prontomarketing.com')
        self.assertEqual(post.number_of_votes, 0)
