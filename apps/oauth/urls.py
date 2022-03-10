from django.urls import path

from .views import  *

urlpatterns = [
    path('token', get_token),
    path('resource', get_resource),
]