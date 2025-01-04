from django.shortcuts import render
from .models import Post

# Create your views here.

def home(req):
    context = {
        "posts" : Post.objects.all()
    }
    return render(req, 'blog/home.html', context)

def about(req):
    return render(req, 'blog/about.html', {'title': 'About'})
