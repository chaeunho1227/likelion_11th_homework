from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .models import Post, Comment
import os

# Create your views here.


def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    # 쿠키를 이용해서 중복적용을 없앨 수 있음. 아직 구현 안되었음.
    post.view_count += 1
    post.save()
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request,'main/detail.html',{
            'post':post,
            'comments':comments,
        })
    
    elif request.method == 'POST':
        new_comment = Comment()
        new_comment.post = post
        new_comment.writer = request.user 
        new_comment.content = request.POST['content'] 
        new_comment.pub_date = timezone.now()
        new_comment.save()
        return redirect('main:detail', id)


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
    if request.user.is_authenticated:
        new_Post = Post()
        new_Post.title = request.POST['title']
        new_Post.writer = request.user
        new_Post.category = request.POST['category']
        new_Post.pub_date = timezone.now()
        new_Post.body = request.POST['body']
        new_Post.image = request.FILES.get('image')
        new_Post.view_count = 0

        new_Post.save()
        return redirect('main:detail', new_Post.id)
    
    else:
        return redirect('accounts:login')


def edit(request, id):
    edit_Post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post': edit_Post})


def update(request, id):
    if request.user.is_authenticated:
        update_Post = Post.objects.get(id=id)
        if request.user == update_Post.writer:
            update_Post.title = request.POST['title']
            update_Post.writer = request.POST['writer']
            update_Post.category = request.POST['category']
            if len(request.FILES) != 0:
                if len(update_Post.image) > 0:
                    os.remove(update_Post.image.path)
                update_Post.image = request.FILES['image']
            update_Post.body = request.POST['body']
            update_Post.pub_date = timezone.now()
            update_Post.save()
            return redirect('main:detail', update_Post.id)
    return redirect('accounts:login')


def delete(request, id):
    delete_Post = Post.objects.get(id=id)
    if len(delete_Post.image) > 0:
        os.remove(delete_Post.image.path)
    delete_Post.delete()
    return redirect('main:mainpage')

def delete_comment(request, id):
    delete_comment = Comment.objects.get(id=id)
    delete_comment.delete()
    return redirect('main:detail',delete_comment.post.id)

def likes(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()
    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
    return redirect('main:detail', post.id)