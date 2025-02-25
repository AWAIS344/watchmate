from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.api import serializers
from rest_framework import status
from rest_framework.authtoken.models import Token
from user_app.api.serializers import RegisterSerializer

# Create your views here.

@api_view(['POST'])
def UserLogout_View(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['POST'])
def UserRegistration(request):
    
    if request.method == 'POST':
        serializers=RegisterSerializer(data=request.data)
        
        if serializers.is_valid():
            user = serializers.save()  # Save user (triggers post_save signal)
            token, created = Token.objects.get_or_create(user=user)  # Fetch the token
            
            return Response({
                'message': 'User registered successfully!',
                'user': serializers.data,
                'token': token.key  # Return the token in the response
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)