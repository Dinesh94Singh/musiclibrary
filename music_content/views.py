from django.http import HttpResponse


def index(request):
    return HttpResponse('<h2> Welcome with music_content </h2> ')
