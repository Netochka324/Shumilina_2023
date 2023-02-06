from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect


def blog_index(request):
    vse_posti = Post.objects.all()
    return render(
        request,
        "blog_index.html",
        {"vse_posti": vse_posti}
    )


def blog_detail(request, pk):
    odin_post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            my_comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=odin_post
            )
            my_comment.save()
            return HttpResponseRedirect(f'/blog/{pk}')
    comments = Comment.objects.filter(post=odin_post)
    context = {
        'odin_post': odin_post,
        'comments': comments,
        'form': form
    }  # закидываем в переменную словарь
    return render(request, 'blog_detail.html', context)


def blog_category_0(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category).order_by("-created_on")
    return render(
        request,
        "blog_category.html",
        {"posts": posts, "category": category}
    )
