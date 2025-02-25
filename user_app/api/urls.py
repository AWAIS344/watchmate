from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path 
from .views import UserRegistration_View,UserLogout_View

urlpatterns = [
    path("login/", obtain_auth_token,name="login"),
    path('register/',UserRegistration_View,name='register'),
    path('logout/',UserLogout_View,name='register')
]
