from django.http import HttpResponse
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()

    html = ''
    for album in all_albums:
        url = '/music_context/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse('<h2> Welcome with music_content </h2> ')


def detail(request, album_id):
    all_songs = Song.objects.all()
    html = ''
    for song in all_songs:
        url = '/music/context/' + str(song.id) + '/'
        html += '<a href="' + url + '">' + song.song_title + '</a><br>'
    return HttpResponse('<h2> Welcome to detail_page of ' + str(album_id) + '</h2>')
