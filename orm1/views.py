from django.shortcuts import render

# Create your views here.

# >>> from orm1.models import Album,Song
# >>> a = Album(title = "Divide", artist = "Ed Sheeran",genre = "Pop")
# >>> a.save()
# >>> s = Song(name = "castle on the hill",album = a)
# >>> s.save()
# >>> a = Album(title = "Abbey Road", artist = "The Beatles",genre = "")
# >>> a = Album(title = "Abbey Road", artist = "The Beatles",genre = "Rock")
# >>> a.save()
# >>> a = Album(title = "Revolver", artist = "The Beatles",genre = "Rock")
# >>> a.save()
# >>> Album.objects.all()
# <QuerySet [<Album: Divide>, <Album: Abbey Road>, <Album: Revolver>]>
# >>> Album.objects.filter(artist = "The Beatles")
# <QuerySet [<Album: Abbey Road>, <Album: Revolver>]>
# >>> Album.objects.exclude(genre = "Rock")
# <QuerySet [<Album: Divide>]>
# >>> Album.objects.get(pk = 3)
# <Album: Revolver>
# >>> Album.objects.get(id = 3)
# <Album: Revolver>
# >>> a = Album.objects.get(pk = 3)
# >>> a.genre = "Pop"
# >>> a.save()
# >>> a.Album.objects.get(pk = 2)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'Album' object has no attribute 'Album'
# >>> a = Album.objects.get(pk = 2)
# >>> a.delete()
# (1, {'orm1.Album': 1})
# >>> Album.objects.all()
# <QuerySet [<Album: Divide>, <Album: Revolver>]>
# >>> Album.objects.filter(genre = "Pop").delete()
# (3, {'orm1.Song': 1, 'orm1.Album': 2})
# >>> Album.objects.all()
# <QuerySet []>
