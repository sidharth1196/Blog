from django.shortcuts import render
from blogs.models import Blog

# Create your views here.
def index(request):
    recent_blogs = Blog.objects.all().order_by('-date')[:15]
    print(len(recent_blogs))
    return render(request, 'blogs/home.html', {'recent_blogs': recent_blogs})