from django.conf.urls import url
from . import views


# namespacing
app_name = 'music'
# /music_content/ for first url
# /music_content/123/ for second url
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]

# what does the above regex say ?
# It wants us to consider a number and pass it as album_id to views detail function
