from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'post'
urlpatterns = [
    url(r'^publish/$', views.publish, name='publish'),
    url(r'^all/$', views.all_posts, name='all_posts'),
    url(r'^api/$', views.PostSerial.as_view(), name='api'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
