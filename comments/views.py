# coding: utf-8
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from blog.models import Post

from .models import Comment
from .forms import CommentForm


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            #当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            #然后重定向到 get_absolute_url 方法返回的 URL。
            #既可以接收一个 URL 作为参数，也可以接收一个模型的实例作为参数
            #如果接收一个模型的实例，那么这个实例必须实现了 get_absolute_url 方法
            return redirect(post)

        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)