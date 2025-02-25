from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path 
from .views import UserRegistration

urlpatterns = [
    path("login/", obtain_auth_token,name="login"),
    path('register/',UserRegistration,name='register')
]
