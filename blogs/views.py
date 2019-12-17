from django.shortcuts import render
from blogs.models import Blog

# Create your views here.
def index(request):
    recent_blogs = Blog.objects.all().order_by('-date')[:15]
    #print(len(recent_blogs))
    return render(request, 'blogs/home.html', {'recent_blogs': recent_blogs})

def blog_details(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/blog_details.html', {'blog':blog})

def all_blogs(request):
    all_blogs = Blog.objects.all().order_by('-date')
    return render(request, 'blogs/all_blogs.html', {'blogs': all_blogs})