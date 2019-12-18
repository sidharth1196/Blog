from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blogs'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('blogs/<int:blog_id>', views.blog_details, name='blog_details'),
    path('allblogs', views.all_blogs, name='all_blogs'),
    path('blogs/create', views.create_blog, name='create_blog'),
]