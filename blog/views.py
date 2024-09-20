from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, 'index.html', context)

def postagem(request, id):
    post = Post.objects.get(pk=id)
    context = {
        "post": post,
    }
    return render(request, 'post.html', context)