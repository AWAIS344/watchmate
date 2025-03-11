from rest_framework import serializers,generics,viewsets
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from watchlist_app.models import Reviews,WatchList, StreamPlatform
from .serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from watchlist_app.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from .throttling import ReviewCreateThrottle, ReviewListThrottle
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import filters
from .pagination import WatchlistPagination




class StreamPlatformVS(viewsets.ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer


# class StreamPlatformVS(viewsets.ViewSet):
#     permission_classes=[IsAdminOrReadOnly]
#     def list(self,request):
#         queryset=StreamPlatform.objects.all()
#         serializers=StreamPlatformSerializer(queryset,many=True,context={'request': request})
#         return Response(serializers.data)
    
#     def retrieve(self,request,pk=None):
#         queryset=StreamPlatform.objects.all()
#         watchlist=get_object_or_404(queryset,pk=pk)
#         serializers=StreamPlatformSerializer(watchlist)
#         return Response(serializers.data)


class ReviewCreate(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Reviews.objects.all()
    serializer_class=ReviewSerializer
    throttle_classes=[ReviewCreateThrottle]


    def perform_create(self, serializer):

        pk = self.kwargs.get('pk')

        user=self.request.user
        movie=WatchList.objects.get(pk=pk)
        review_queryset=Reviews.objects.filter(review_user=user,watchlist=movie)
        
        if review_queryset.exists():
            raise ValidationError("Yoo already had reviewed this Movie")
        
        if movie.no_of_rating == 0:
            movie.avg_rating=serializer.validated_data['rating']
        else:
            movie.avg_rating=(movie.avg_rating + serializer.validated_data['rating'] )/2

        movie.no_of_rating+=1
        movie.save()
        serializer.save(watchlist=movie,review_user=user)


class ReviewList(generics.ListAPIView):
    # authentication_classes=[bas] 
    # permission_classes=[IsAuthenticated]   #Object Level Permissions
    serializer_class=ReviewSerializer
    throttle_classes=[ReviewListThrottle]
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["review_user__username","active"]


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
    permission_classes=[IsReviewUserOrReadOnly]
    queryset=Reviews.objects.all()
    serializer_class=ReviewSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope="review-details"



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
    permission_classes=[IsAdminOrReadOnly]
    queryset=WatchList.objects.all()
    serializer_class=WatchListSerializer
    # filter_backends = [filters.SearchFilter]
    filter_backends = [filters.OrderingFilter]
    # search_fields = ['title', 'genre',]
    ordering_fields = ['avg_rating']
    pagination_class = WatchlistPagination

class WATCHDETAILSAC(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdminOrReadOnly]
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
    permission_classes=[IsAdminOrReadOnly]
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer

class PlatformDetailsAC(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdminOrReadOnly]
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
    

    
