from django.shortcuts import render
from .models import Post, Category, Comment


def blog_index(request):
    vse_posti = Post.objects.all()
    return render(
        request,
        "blog_index.html",
        {"vse_posti": vse_posti}
    )


def blog_detail(request, pk):
    odin_post = Post.objects.get(pk=pk)
    comment = Comment.objects.filter(post=odin_post)
    post_category = Category.objects.filter(pk=pk)
    return render(
        request,
        "blog_detail.html",
        {"odin_post": odin_post, "comment": comment, "post_category": post_category}
    )


def blog_category_1(request):
    posts = Post.objects.all()
    return render(
        request,
        "blog_category1.html",
        {"posts": posts}
    )


def blog_category_2(request):
    posts = Post.objects.all()
    return render(
        request,
        "blog_category1.html",
        {"posts": posts}
    )


def blog_category_3(request):
    posts = Post.objects.all()
    return render(
        request,
        "blog_category3.html",
        {"posts": posts}
    )


def blog_category_0(request, category):
    posts = Post.objects.all()
    categories = Category.objects.get(post_category=category)
    return render(
        request,
        "blog_category.html",
        {"posts": posts, "categories": categories}
    )
