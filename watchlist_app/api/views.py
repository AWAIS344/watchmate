from rest_framework import serializers,generics,viewsets
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from watchlist_app.models import Reviews,WatchList, StreamPlatform
from .serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer



class StreamPlatformVS(viewsets.ModelViewSet):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer


class StreamPlatformVS(viewsets.ViewSet):
    def list(self,request):
        queryset=StreamPlatform.objects.all()
        serializers=StreamPlatformSerializer(queryset,many=True,context={'request': request})
        return Response(serializers.data)
    
    def retrieve(self,request,pk=None):
        queryset=StreamPlatform.objects.all()
        watchlist=get_object_or_404(queryset,pk=pk)
        serializers=StreamPlatformSerializer(watchlist)
        return Response(serializers.data)


class ReviewCreate(generics.CreateAPIView):
    queryset=Reviews.objects.all()
    serializer_class=ReviewSerializer


    def perform_create(self, serializer):

        pk = self.kwargs.get('pk')

        user=self.request.user
        movie=WatchList.objects.get(pk=pk)
        review_queryset=Reviews.objects.filter(review_user=user,watchlist=movie)
        
        if review_queryset.exists():
            raise ValidationError("Yoo already had reviewed this Movie")
        serializer.save(watchlist=movie,review_user=user)


class ReviewList(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ReviewSerializer

    def get_queryset(self):
        pk=self.kwargs['pk']
        return Reviews.objects.filter(watchlist=pk)



    
# class ReviewDetails(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset=Reviews.objects.all()
#     serializer_class=ReviewSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(generics.ListCreateAPIView):
#     queryset=Reviews.objects.all()
#     serializer_class=ReviewSerializer


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Reviews.objects.all()
    serializer_class=ReviewSerializer



# class WATCHLISTAV(APIView):

#     def get(self,request):
#         movie=WatchList.objects.all()
#         serializers=WatchListSerializer(movie,many=True)
#         return Response(serializers.data)
    

#     def post(self, request):
#         serializer = WatchListSerializer(data=request.data)  
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)  

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class   WATCHLISTAV(generics.ListCreateAPIView):
    queryset=WatchList.objects.all()
    serializer_class=WatchListSerializer

class WATCHDETAILSAC(generics.RetrieveUpdateDestroyAPIView):
    queryset=WatchList.objects.all()
    serializer_class=WatchListSerializer


# class WATCHDETAILSAC(APIV):

#     def get(self,request,pk):
#         movie=WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(movie)

#         return Response(serializer.data)


#     def put(self,request,pk):
#         movie =WatchList.objects.get(pk=pk)
#         serializers=WatchListSerializer(movie,data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     def delete(self,request,pk):
#         movie=WatchList.objects.get(pk=pk)
#         movie.delete()
#         return Response({"message":"Movie deleted"})


class PlatformAC(generics.ListCreateAPIView):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer

class PlatformDetailsAC(generics.RetrieveUpdateDestroyAPIView):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer


    

# class PlatformAC(APIView):

#     def get(self,request):
#         stream=StreamPlatform.objects.all()
#         serializer=StreamPlatformSerializer(stream,many=True,context={'request': request})

#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=StreamPlatformSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
# class PlatformDetailsAC(APIView):

#     def get(self,request,pk):
#         try:
#             stream = StreamPlatform.objects.get(pk=pk)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer=StreamPlatformSerializer(stream,context={'request': request})
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         stream=StreamPlatform.objects.get(pk=pk)
#         serializer=StreamPlatformSerializer(stream,data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data)
#         return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
#     def delete(self,request,pk):
#         stream=StreamPlatform.objects
    

    
