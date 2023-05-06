from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404

from .models import Post, Comment, Like
from .forms import CommentForm, PostForm



def post_list(request):
    posts = Post.objects.all().annotate(
        likes_count=Count('likes'),
        comments_count=Count('comments')
    )

    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if the user is authenticated
    if request.user.is_authenticated:
        liked = Like.objects.filter(user=request.user, post=post).exists()
    else:
        liked = False

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'liked': liked,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    
    context = {
        'form': form
    }

    return render(request, 'blog/add_comment.html', context)


def is_staff(user):
    return user.is_staff


@user_passes_test(is_staff, login_url='/blog/')
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    context = {
        'form': form
    }

    return render(request, 'blog/post_create.html', context)


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    liked = Like.objects.filter(user=request.user, post=post)
    if liked.exists():
        liked.delete()
    else:
        Like.objects.create(user=request.user, post=post)
    return redirect('post_detail', pk=post.pk)


@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    post_pk = comment.post.pk

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post_pk)

    form = CommentForm(instance=comment)

    context = {
        'form': form,
        'comment': comment
    }
    return redirect('post_detail', pk=post_pk)


@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    post_pk = comment.post.pk

    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', pk=post_pk)

    return redirect('post_detail', pk=post_pk)