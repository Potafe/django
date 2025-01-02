from django.shortcuts import render

# Create your views here.

posts = [
    {
        "author": "yazat",
        "title": "First Post",
        "content": "Hello World",
        "date": "2 Jan 2025"
    },
    {
        "author": "Shiv",
        "title": "Second Post",
        "content": "Hello Universe",
        "date": "2 Jan 2025"
    }
]

def home(req):
    context = {
        "posts" : posts
    }
    return render(req, 'blog/home.html', context)

def about(req):
    return render(req, 'blog/about.html', {'title': 'About'})
