from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import authenticate

from .serializers import AccountSerializer
from .models import Account

import random
import string

@api_view(['POST'])
def register(request):
    serializer = AccountSerializer(data=request.data)
    print()
    if serializer.is_valid():
        data = serializer.validated_data
        serializer.save()
        account = Account.objects.get(username=data['username'])
        account.client_id = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))
        account.sclient_secret = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(32))
        account.save()
        response = {
            'status' : 201,
            'username' : data['username'],
            'npm' : data['npm'],
            'fullname' : data['fullname'],
            'client_id' : account.client_id,
            'client_secret' : account.client_secret,
            'message' : 'Account successfully created'
        }
        return Response(response, status=status.HTTP_201_CREATED)
    response = {
        'status' : 400,
        'message' : serializer.errors
    }

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        response = {
            'status' : 400,
            'message' : 'Please provide both username and password'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    if not user:
        response = {
            'status' : 400,
            'message' : 'Wrong username/password'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    response = {
        'status' : 200,
        'message' : 'OK'
    }
    return Response(response, status=status.HTTP_200_OK)