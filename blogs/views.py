from django.shortcuts import render
from blogs.models import Blog
from users.models import Author
import datetime

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

def create_blog(request):
    created = False
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        author = Author.objects.get(user__id = request.user.id)
        #print(author.first_name)
        blog = Blog.objects.create(title = title, date = datetime.datetime.now(), body = body, author = author)
        created = True
    return render(request, 'blogs/createblog.html', {'created':created})