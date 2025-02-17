from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render

from .views import WATCHLISTAV,WATCHDETAILSAC,PlatformAC,PlatformDetailsAC,ReviewList,ReviewDetails

urlpatterns = [
    path("list/",WATCHLISTAV.as_view(),name="watchlist"),
    path("list/<int:pk>",WATCHDETAILSAC.as_view(),name="moviedetails"),
    path("streamlist/",PlatformAC.as_view(),name="platformsav"),
    path("streamlist/<int:pk>",PlatformDetailsAC.as_view(),name="platformdetails"),

    path("review/",ReviewList.as_view(),name="reviews"),
    path("review/<int:pk>",ReviewDetails.as_view(),name="reviews_details")

]
