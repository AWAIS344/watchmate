from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from watchlist_app import models
from .serializers import WatchListSerializer

class WATCHLISTAV(APIView):

    def get(self,request):
        movie=models.WatchList.objects.all()
        serializers=WatchListSerializer(movie,many=True)
        return Response(serializers.data)
    

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)  # ✅ Fixed variable name (not "serializers")
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # ✅ 201 for success

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # ✅ 400 for errors

    


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
    
    def patch(self,request,pk):
        movie=models.WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer()
        movie=serializer.toogle(movie)

        return Response({'message':"Status Updated Successfully","pulished":movie.published})

    


# @api_view(['GET','POST'])
# def watchlist(request):

#     if request.method == 'POST':
#         serializer = WatchSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         movies = models.Movie.objects.all()
#         serializers = WatchSerializer(movies,many=True)
#         return Response(serializers.data)


# @api_view(['GET','PUT','DELETE','PATCH'])
# def moviedetails(request,pk):

#     if request.method == 'GET':
#         movie = models.Movie.objects.get(pk=pk)
#         serializer = WatchSerializer(movie)

#         return Response(serializer.data)
#     if request.method == 'PUT':
#         movie = models.Movie.objects.get(pk=pk)
#         serializer = WatchSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_404_NOT_FOUND)
    

#     if request.method == 'DELETE':
#         movie = models.Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response({"message":"Movie deleted"})
    
#     if request.method=='PATCH':
#         movie=models.Movie.objects.get(pk=pk)
#         serializer=WatchSerializer()
#         movie=serializer.toogle(movie)

#         return Response({'message':"Status Updated Successfully","pulished":movie.published})


        
