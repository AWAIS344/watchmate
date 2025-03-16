from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from rest_framework.routers import DefaultRouter


from .views import WATCHLISTAV,WATCHDETAILSAC,PlatformAC,PlatformDetailsAC,ReviewList,ReviewDetails,ReviewCreate,StreamPlatformVS, UserReview

router=DefaultRouter()

router.register("stream",StreamPlatformVS,basename="streamplatform")

urlpatterns = [
    path("list/",WATCHLISTAV.as_view(),name="watchlist"),
    path("<int:pk>",WATCHDETAILSAC.as_view(),name="moviedetails"),
    # path("stream/",PlatformAC.as_view(),name="platformsav"),
    # path("stream/<int:pk>",PlatformDetailsAC.as_view(),name="platformdetails"),


    path("<int:pk>/review-create",ReviewCreate.as_view(),name="review_create"),
    path("review/<int:pk>",ReviewDetails.as_view(),name="review_detail"),
    path("<int:pk>/review/",ReviewList.as_view(),name="review_list"),
    path("",include(router.urls)),

    path("reviews/",UserReview.as_view(),name="user_review_list"),
    

]
