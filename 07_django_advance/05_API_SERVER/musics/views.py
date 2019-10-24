from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Artist, Music
from .serializers import ArtistSerializer, MusicSerializer, ArtistDetailSerializer

from IPython import embed
# import json

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    serializer = ArtistDetailSerializer(artist)

    return Response(serializer.data)

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    ser = MusicSerializer(music)
    return Response(ser.data)

    # dataset = []
    # for artist in artists:
    #     d = {
    #         "id": artist.id,
    #         "name": artist.name,
    #     }
    #     dataset.append(d)
    
    # res_data = json.dumps(dataset)
    # # dictionary를 공용어로 바꾸다. (Serialization : 직렬화)
    # return HttpResponse(res_data)