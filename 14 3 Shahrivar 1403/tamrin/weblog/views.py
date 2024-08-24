from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import BlogPost


def show_weblogs_homepage(request):
    posts = BlogPost.objects.all().filter(status='pu').order_by('-datetime_modified')
    context = {
        'posts': posts,
    }
    return render(request, 'blog.html', context)


def show_weblogs_detail(request, pk):
    post = get_object_or_404(BlogPost, id=pk)
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)


def new_post(request):
    if request.method=='POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        user = get_user_model().objects.first()
        BlogPost.objects.create(author=user, title=title, description=text, status='pu')
    return render(request, 'new_post.html')



def about_us(request):
    return render(request, 'about_us.html')
