from django.urls import path

from .views import  *

urlpatterns = [
    path('create', create),
    path('<str:course_id>', read),
    path('update/<str:course_id>', update),
    path('delete/<str:course_id>', delete)
]