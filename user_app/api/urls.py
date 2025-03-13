from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path 
from .views import UserRegistration_View,UserLogout_View
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path("login/", obtain_auth_token,name="login"),
    path('register/',UserRegistration_View,name='register'),
    path('logout/',UserLogout_View,name='logout'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
