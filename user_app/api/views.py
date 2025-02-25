from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import serializers
from user_app.api.serializers import RegisterSerializer

# Create your views here.

@api_view(['POST'])
def UserRegistration(request):
    
    if request.method == 'POST':
        serializers=RegisterSerializer(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)