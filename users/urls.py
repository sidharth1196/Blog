from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'signup', views.register, name='register'),
    url(r'login', views.user_login, name='login'),
    url(r'logout', views.user_logout, name='logout')
]