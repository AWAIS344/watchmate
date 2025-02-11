from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render

from .views import WATCHLISTAV,WATCHDETAILSAC

urlpatterns = [
    path("list/",WATCHLISTAV.as_view(),name="watchlist"),
    path("list/<int:pk>",WATCHDETAILSAC.as_view(),name="moviedetails"),
]
