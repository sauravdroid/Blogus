from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import *


def blog_page(request):
    return render(request, 'User/blog_page.html', {'title': 'Blog Page'})


def publish_post(request):
    return render(request, 'User/publish_page.html', {'title': 'Publish Story'})


def login(request):
    if request.method == 'GET':
        return render(request, 'User/login.html', {'bar': 'false', 'title': 'Login Page'})

    else:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if len(username) == 0 or len(password) == 0:
            return HttpResponse('Wrong Username or Password')
        return HttpResponse(username + ' ' + password)


def all_posts(request):
    return render(request, 'User/posts.html', {'title': 'All Post'})


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return HttpResponse("Successfully Registered")
    else:
        raise Http404("Page not Found error")
