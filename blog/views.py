from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'title': 'Post 1',
        'content': 'This is post 1',    
    },
    {
        'title': 'Post 2',
        'content': 'This is post 2',    
    }
]

# Create your views here.
#def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

#def about(request):
   # return HttpResponse('<h1>Blog About</h1>')

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

