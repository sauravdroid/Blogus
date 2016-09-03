from django.conf.urls import url
from . import views

app_name = 'user'
urlpatterns = [
    url(r'^$', views.blog_page, name='blog_page'),
    url(r'^publish$', views.publish_post, name='blog_page'),
    url(r'^login$', views.user_login, name='login'),
    url(r'^all$', views.all_posts, name='all_posts'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout', views.logout_user, name='logout'),
]
