from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from watchlist_app import models
from .serializers import WatchListSerializer,StreamPlatformSerializer
class WATCHLISTAV(APIView):

    def get(self,request):
        movie=models.WatchList.objects.all()
        serializers=WatchListSerializer(movie,many=True)
        return Response(serializers.data)
    

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)  
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class WATCHDETAILSAC(APIView):

    def get(self,request,pk):
        movie=models.WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie)

        return Response(serializer.data)


    def put(self,request,pk):
        movie =models.WatchList.objects.get(pk=pk)
        serializers=WatchListSerializer(movie,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        movie=models.WatchList.objects.get(pk=pk)
        movie.delete()
        return Response({"message":"Movie deleted"})
    

class PlatformAC(APIView):

    def get(self,request):
        stream=models.StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(stream,many=True)

        return Response(serializer.data)
    
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
class PlatformDetailsAC(APIView):

    def get(self,request,pk):
        try:
            stream = models.StreamPlatform.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=StreamPlatformSerializer(stream)
        return Response(serializer.data)

    
