from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render

from .views import MOVIELISTAV,MOVIEDETAILSAC

urlpatterns = [
    path("list/",MOVIELISTAV.as_view(),name="watchlist"),
    path("list/<int:pk>",MOVIEDETAILSAC.as_view(),name="moviedetails"),
]
