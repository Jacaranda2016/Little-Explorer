from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.core.paginator import *
from django.template import Context, loader

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    post = posts[0]
    abouts = Post.objects.filter(shortUrl='who-is-little-explorer')
    about = abouts[0]
    return render(request, 'volton/index.html', {'posts': posts, 'post': post, 'about': about})

def article(request, shortUrl):
    posts = Post.objects.filter(shortUrl=shortUrl)
    post = posts[0]
    return render(request, 'volton/article.html', {'post': post})


def articles(request, page=1):
    after_range_num = 5
    bevor_range_num = 4
    if page == None:
        page = 1
    else:
        page = int(page)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(posts, 2)
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        posts = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num:page + bevor_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + bevor_range_num]
    return render(request, 'volton/wholeList.html', {'posts': posts, 'page_range': page_range})