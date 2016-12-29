from django.conf.urls import url
from . import views


# name spacing
app_name = 'music'

# /music_content/ for first url
# /music_content/<album_id>/ for second url
# /music_content/<album_id>/favorite/
# third url is for logic filled url
# (like a url for logout where logout code should happen and another/home page gets loaded)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]

# what does the above regex say ?
# It wants us to consider a number and pass it as album_id to views detail function
