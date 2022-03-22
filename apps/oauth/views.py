from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import FormParser
from rest_framework import authentication

from django.contrib.auth import authenticate
from django.db.utils import IntegrityError

from .models import OAuth
from .utils import validation

import random
import string
import hashlib
from datetime import datetime, timedelta

@api_view(['POST'])
@parser_classes([FormParser])
def get_token(request):
    username = request.data.get('username')
    password = request.data.get('password')
    client_id = request.data.get('client_id')
    client_secret = request.data.get('client_secret')

    if username and password:
        user = authenticate(username=username, password=password)
        if user and client_id == user.client_id and client_secret == user.client_secret:
            refresh_token = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(40))
            current_time = datetime.now()
            data = {
                'username' : username,
                'password' : password,
                'current_time' : current_time
            }
            access_token = hashlib.sha1(str(data).encode()).hexdigest()
            try:
                oauth = OAuth.objects.create(account=user, access_token=access_token, refresh_token=refresh_token)
            except IntegrityError:
                oauth = OAuth.objects.get(account=user)
                oauth.access_token=access_token
                oauth.refresh_token=refresh_token
            oauth.save()
            response = {
                'access_token' : access_token,
                'expires_in' : 300,
                'token_type' : 'Bearer',
                'scope' : None,
                'refresh_token' : refresh_token,
            }
            return Response(response, status=status.HTTP_200_OK)

    response = {
        'error' : 'invalid_request',
        'Error_description' : 'ada kesalahan masbro!',
    }
    return Response(response, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@parser_classes([FormParser])
def get_resource(request):
    try: 
        oauth = validation(request)
        access_token = oauth.access_token
        refresh_token = oauth.access_token
        account = oauth.account
        full_name = account.fullname
        user_id = account.username
        client_id = account.client_id
        npm = account.npm
        response = {
            'access_token' : access_token,
            'client_id' : client_id,
            'user_id' : user_id,
            'full_name' : full_name,
            'npm' : npm,
            'expires' : None,
            'refresh_token' : refresh_token,
        }
        return Response(response, status=status.HTTP_200_OK)

    except (authentication.exceptions.AuthenticationFailed):
        response = {
            'error' : 'invalid_token',
            'error_description' : 'Token Salah masbro'
        }
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)