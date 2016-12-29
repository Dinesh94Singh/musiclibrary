from django.http import Http404
from .models import Album
from django.shortcuts import render


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    # context is the information our template needs
    return render(request, 'music_content/index', context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=int(album_id))
    except Exception:
        raise Http404(" Album not Found !! ")
    context = {'album': album}
    return render(request, 'music_content/detail.html', context)
