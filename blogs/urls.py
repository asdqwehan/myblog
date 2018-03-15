from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^titles/$', views.titles, name='titles'),
    url(r'^titles/(?P<title_id>\d+)/$', views.title, name='title'),
    url(r'^new_blog/$', views.new_blog, name='new_blog'),
    url(r'^titles/(?P<title_id>\d+)/edit_blog/$', views.edit_blog, name='edit_blog'),
    url(r'^titles/(?P<title_id>\d+)/reply/$', views.reply, name='reply'),
]
