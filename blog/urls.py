from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'blog'
urlpatterns = [        
    url(r'^$', views.welcome, name='welcome'),
    url(r'^home', views.home, name='home'),
    url(r'^food', views.food, name='food'),
    url(r'^index', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^search/$', views.search, name='search'),
    
]

