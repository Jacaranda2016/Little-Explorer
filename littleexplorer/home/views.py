from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'index.html', {'posts':posts})

# Create your views here.
def volton(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'volton/index.html', {'posts':posts})

def article(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'volton/article.html', {'posts':posts})

def articles(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'volton/articles.html', {'posts':posts})