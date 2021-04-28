from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.forms import PostForm
from blog.models import Post, Comment


def get_profile(httpRequest):
    return HttpResponse('Hello World')


def get_my_age(httpRequest):
    return HttpResponse('24')


def get_posts(request):
    method_post = request.method
    if method_post == 'POST':
        post = Post.objects.create(title='Good Morning',
                                   description='Have a good day')
        return HttpResponse('Put to the our posts')
    elif method_post == 'GET':
        post_all = Post.objects.all()
        return HttpResponse(post_all)
    elif method_post == 'DELETE':
        post = Post.objects.get(id=1)
        post.delete()
        return HttpResponse('This post deleted')
    elif method_post == 'PUT':
        post = Post.objects.get(id=1)
        post.title = 'Good Evening'
        post.description = 'Good night'
        post.save()
        return HttpResponse('This post was changed successfully')


def get_all_posts(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/posts_list.html', context)


class PostView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/posts_detail.html'


class CommentView(ListView):
    model = Comment
    template_name = 'comment/comment_list.html'

    def get_queryset(self):
        return Comment.objects.all()


def add_post(request):
    method = request.method
    if method == 'POST':
        form = PostForm(request.POST, request.FILES)
        Post.objects.create(
            title=form.data['title'],
            description=form.data['description'],
            image=form.data['image'])
        return HttpResponse('Post created')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})