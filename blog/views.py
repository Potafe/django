from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
def home(req):
    context = {
        "posts" : Post.objects.all()
    }
    return render(req, 'blog/home.html', context)

def about(req):
    return render(req, 'blog/about.html', {'title': 'About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'