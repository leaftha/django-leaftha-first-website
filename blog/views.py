from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic import ListView

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')


# def index(requst):
#    posts = Post.objects.all()
#    return render(
#        requst,
#        'blog/index.html',
#        {
#            'posts': posts,
#        }
#
#    )