from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from django.contrib import messages

from .forms import PostForm


def post(request):
    """A view to show all blog posts"""
    posts = Post.objects.all()

    template = "blogs/blogs.html"
    context = {
        "posts": posts,
    }

    return render(request, template, context)


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)

    template = "blogs/blog_detail.html"
    context = {
        "post": post,
    }

    return render(request, template, context)


def add_post(request):
    """A view to allow the site owner to add an blog post"""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Post Added")
            return redirect(reverse("post_detail", args=[post.slug]))
        else:
            messages.error(request, "NOPE")
    else:
        form = PostForm()

    template = "blogs/add_blog.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


def edit_post(request, slug):
    """A view to delete an blog post"""
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated blog")
            return redirect(reverse("post_detail", args=[post.slug]))
        else:
            messages.error(request, "Failed to update the blog.")
    else:
        form = PostForm(instance=post)
        messages.info(request, f"You are editing {post.title}")

    template = "blogs/edit_blog.html"
    context = {
        "form": form,
        "post": post,
    }

    return render(request, template, context)


def delete_post(request, slug):
    """Delete a blog"""

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "blog deleted!")
    return redirect(reverse("blogs"))
