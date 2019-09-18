from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

class PostDetail(DetailView):
    model = Post


# def post_detail (request, pk):
#     blog_post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'blog_post': blog_post,
#         }
#     )


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