from django.conf.urls import url
from . import views

app_name = 'user'
urlpatterns = [
    url(r'^$', views.blog_page, name='blog_page'),
    url(r'^publish$', views.publish_post, name='blog_page'),
    url(r'^login', views.login, name='login'),
    url(r'^all', views.all_posts, name='all_posts'),
    url(r'^dummy', views.dummy_response, name='dummy'),
]
