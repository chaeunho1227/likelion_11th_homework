from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.


def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.view_count += 1
    post.save()
    return render(request, 'main/detail.html', {'post': post})


def mainpage(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html', {'posts': posts})


def secondpage(request):
    return render(request, 'main/secondpage.html')


def chaeunho(request):
    return render(request, 'main/chaeunho.html')


def new_post(request):
    return render(request, 'main/new_post.html')


def create(request):
    new_Post = Post()
    new_Post.title = request.POST['title']
    new_Post.writer = request.POST['writer']
    new_Post.category = request.POST['category']
    new_Post.pub_date = timezone.now()
    new_Post.body = request.POST['body']
    new_Post.view_count = 0

    new_Post.save()

    return redirect('detail', new_Post.id)
