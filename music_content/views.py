from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView


# we also have UpdateView, DeleteView


'''
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    # context is the information our template needs
    return render(request, 'music_content/index.html', context)


    try:
        album = Album.objects.get(pk=album_id)
    except Exception:
        raise Http404(" Album not Found !! ")


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {'album': album}
    return render(request, 'music_content/detail.html', context)


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        context = {
            'album': album,
            'error_message': 'You did not select any song, Please select'
        }
        return render(request, 'music_content/detail.html', context)
    else:
        selected_song.is_favorite = True
        selected_song.save()
        context = {'album': album}
        return render(request, 'music_content/detail.html', context)
'''

# there are lot of generic view, in this we are using
# list generic view and detail generic view

# index is list generic view


class IndexView(generic.ListView):
    template_name = 'music_content/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music_content/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
