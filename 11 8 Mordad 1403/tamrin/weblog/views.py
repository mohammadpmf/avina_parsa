from django.shortcuts import render

from .models import BlogPost

def show_weblogs_homepage(request):
    posts = BlogPost.objects.all().filter(status='pu').order_by('-datetime_modified')
    context = {
        'posts': posts,
    }
    return render(request, 'blog.html', context)