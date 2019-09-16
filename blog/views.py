from django.shortcuts import render
from .models import Post
# Create your views here.



def index(requst):
    posts = Post.objects.all()
    return render(
        requst,
        'blog/index.html',
        {
            'posts': posts,
        }

    )