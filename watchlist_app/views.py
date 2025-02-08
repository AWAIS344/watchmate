# from django.shortcuts import render
# from watchlist_app import models
# from django.http import JsonResponse

# # Create your views here.

# def watchlist_view(request):
#     watchlist = models.Movie.objects.all()
#     data={"watchlist":list(watchlist.values())}

#     return JsonResponse(data)

 
# def movie_detail(request,pk):
#     movie = models.Movie.objects.get(pk=pk)
#     data={"name":movie.title,"description":movie.about,"genre":movie.genre,}

#     return JsonResponse(data)