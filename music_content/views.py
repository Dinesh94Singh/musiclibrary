from .models import Album
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    # context is the information our template needs
    return render(request, 'music_content/index.html', context)


''' try:
        album = Album.objects.get(pk=album_id)
    except Exception:
        raise Http404(" Album not Found !! ") '''


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {'album': album}
    return render(request, 'music_content/detail.html', context)
