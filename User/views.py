from django.shortcuts import render
from django.http import HttpResponse


def blog_page(request):
    return render(request, 'User/blog_page.html', {'title': 'Blog Page'})


def publish_post(request):
    return render(request, 'User/publish_page.html', {'title': 'Publish Story'})


def login(request):
    return render(request, 'User/login.html', {'bar': 'false', 'title': 'Login Page'})


def all_posts(request):
    return render(request, 'User/posts.html', {'title': 'All Post'})


def dummy_response(request):
    return HttpResponse("This is a dummy response")
