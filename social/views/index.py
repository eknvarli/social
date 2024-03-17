from django.shortcuts import render, redirect
from social.models import Post


def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(is_active=True)

        return render(request, 'social/feed.jinja', context={
            'posts': posts,
        })
    else:
        return redirect('login')