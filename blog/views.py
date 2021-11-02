from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Blog, Post, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CommentForm
from .forms import PostForm


def blog(request):
    """ BLog page to display all available posts """

    posts = Post.objects.all()
    template = 'blog/blog.html'
    context = {
        'posts': posts
    }
    
    return render(request, template, context)

def post_detail(request, slug):
    """ Display each Post in detail along with its comments """
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    template = 'blog/blog_detail.html'
    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)
