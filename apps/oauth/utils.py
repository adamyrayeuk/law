from rest_framework import authentication
from rest_framework.authentication import get_authorization_header

from .models import OAuth

from datetime import datetime, timedelta

def validation(request):
    keywords = ['bearer']
    auth = get_authorization_header(request).split()

    if not auth or auth[0].lower().decode() not in keywords:
        msg = 'Invalid token header. No credentials provided.'
        raise authentication.exceptions.AuthenticationFailed(msg)

    if len(auth) == 1:
        msg = 'Invalid token header. No credentials provided.'
        raise authentication.exceptions.AuthenticationFailed(msg)

    elif len(auth) > 2:
        msg = 'Invalid token header. Token string should not contain spaces.'
        raise authentication.exceptions.AuthenticationFailed(msg)

    try:
        token = auth[1].decode()
    except UnicodeError:
        msg = 'Invalid token header. Token string should not contain invalid characters.'
        raise authentication.exceptions.AuthenticationFailed(msg)

    try:
        oauth = OAuth.objects.get(access_token=token)
    except OAuth.DoesNotExist:
        msg = 'Invalid token'
        raise authentication.exceptions.AuthenticationFailed(msg)

    if (oauth.expired_datetime + timedelta(seconds=300)).timestamp() < datetime.now().timestamp():
        msg = 'Invalid token'
        raise authentication.exceptions.AuthenticationFailed(msg)
    
    return oauth