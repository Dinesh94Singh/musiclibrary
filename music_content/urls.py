from django.conf.urls import url

from . import views

urlpatterns = [
    # /music_content/
    url(r'^$', views.index, name='index'),
    # /music_content/123/
    url(r'^(?P<album_id>[0-9]+/)$', views.detail, name='detail'),
    # homepage for each individual app
]

# what does the above regex say ?
# It wants us to consider a number and pass it as album_id to views detail function
