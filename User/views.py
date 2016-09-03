from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='user:login')
def blog_page(request):
    return render(request, 'User/blog_page.html', {'title': 'Blog Page'})


@login_required(login_url='user:login')
def publish_post(request):
    return render(request, 'User/publish_page.html', {'title': 'Publish Story'})


def user_login(request):
    if request.user.is_authenticated():
        return redirect('user:all_posts')
    else:
        if request.method == 'GET':
            return render(request, 'User/login.html', {'bar': 'false', 'title': 'Login Page'})

        elif request.method == 'POST' and request.is_ajax():
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            if len(username) == 0 or len(password) == 0:
                return HttpResponse('Wrong Username or Password')
            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    if request.GET.get('next'):
                        return JsonResponse(
                            {'success': 'true', 'response': 'User is Authenticated',
                             'success_url': request.GET.get('next')})
                    else:
                        return JsonResponse(
                            {'success': 'true', 'response': 'User is Authenticated', 'success_url': '/all'})
                else:
                    return JsonResponse({'success': 'false', 'response': 'Wrong Username or Password'})


@login_required(login_url='user:login')
def all_posts(request):
    return render(request, 'User/posts.html', {'title': 'All Post'})


def register(request):
    if request.method == 'POST' and request.is_ajax():
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return JsonResponse({'success': 'true', 'response': 'Successfully Registered'})
    else:
        raise Http404("Page not Found error")


@login_required(login_url='user:login', redirect_field_name='')
def logout_user(request):
    logout(request)
    return redirect('user:login')
