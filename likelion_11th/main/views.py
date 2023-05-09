from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
import os

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
    new_Post.image = request.FILES.get('image')
    new_Post.view_count = 0

    new_Post.save()

    return redirect('main:detail', new_Post.id)


def edit(request, id):
    edit_Post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post': edit_Post})


def update(request, id):
    update_Post = Post.objects.get(id=id)
    update_Post.title = request.POST['title']
    update_Post.writer = request.POST['writer']
    update_Post.category = request.POST['category']
    update_Post.pub_date = timezone.now()
    # 이미지 수정
    if len(request.FILES) != 0:
        # 기존 이미지가 있다면 삭제
        if len(update_Post.image) > 0:
            os.remove(update_Post.image.path)
        update_Post.image = request.FILES['image']
    update_Post.body = request.POST['body']
    update_Post.view_count = 0
    update_Post.save()
    return redirect('main:detail', update_Post.id)


def delete(request, id):
    delete_Post = Post.objects.get(id=id)
    if len(delete_Post.image) > 0:
        os.remove(delete_Post.image.path)
    delete_Post.delete()
    return redirect('main:mainpage')
