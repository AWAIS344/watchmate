from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from watchlist_app import models
from .serializers import WatchSerializer 

@api_view()
def watchlist(request):
    movies = models.Movie.objects.all()
    serializers = WatchSerializer(movies,many=True)

    return Response(serializers.data)


@api_view()
def moviedetails(request,pk):
    movie = models.Movie.objects.get(pk=pk)
    serializer = WatchSerializer(movie)

    return Response(serializer.data)