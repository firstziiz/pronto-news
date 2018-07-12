from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse

from .models import Post
from .forms import PostForm


# Create your views here.
class PostListView(TemplateView):
    template_name = 'post_list.html'

    def get(self, request):
        posts = Post.objects.all()

        form = PostForm()

        return render(request, self.template_name, {
            'posts': posts,
            'form': form
        })

    def post(self, request):
        form = PostForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('post_list'))
