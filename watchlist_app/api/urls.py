from django.contrib import admin
from django.urls import path,include

from .views import watchlist,moviedetails

urlpatterns = [
    path("list/",watchlist,name="watchlist"),
    path("list/<int:pk>",moviedetails,name="moviedetails"),
]
