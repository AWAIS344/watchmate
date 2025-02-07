from django.shortcuts import render
from watchlist_app import models

# Create your views here.

def watchlist_view(request):
    watchlist = models.Watchlist.objects.all()
    context= {'watchlist': watchlist}
    return render(request, 'watchlist_app/watchlist.html',context)
