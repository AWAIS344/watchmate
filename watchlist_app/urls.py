from django.contrib import admin
from django.urls import path
from watchlist_app.views import *

urlpatterns = [
    path("list/" ,watchlist_view,name="movie_list"),
    path("list/<int:pk>", movie_detail, name="movie_detail"),
    path("admin/", admin.site.urls),
]
