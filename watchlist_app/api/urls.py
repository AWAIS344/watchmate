from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render

from .views import WATCHLISTAV,WATCHDETAILSAC,PlatformAC,PlatformDetailsAC,ReviewList,ReviewDetails,ReviewCreate

urlpatterns = [
    path("list/",WATCHLISTAV.as_view(),name="watchlist"),
    path("list/<int:pk>",WATCHDETAILSAC.as_view(),name="moviedetails"),
    path("stream/",PlatformAC.as_view(),name="platformsav"),
    path("stream/<int:pk>",PlatformDetailsAC.as_view(),name="platformdetails"),


    path("stream/<int:pk>/review-create",ReviewCreate.as_view(),name="review_create"),
    path("stream/review/<int:pk>",ReviewDetails.as_view(),name="review_detail"),
    path("stream/<int:pk>/review",ReviewList.as_view(),name="review_list")
    

]
