from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


# Create your views here.
class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        html = '<ul>'
        for each in posts:
            html += f'<li><a href="{each.url}">{each.title}</a></li>'
        html += '</ul>'
        return HttpResponse(html)