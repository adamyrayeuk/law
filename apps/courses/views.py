from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course

import json

@api_view(['POST'])
def create(request):
    try:
        data = json.loads(request.data.get('_content'))
    except TypeError:
        data = request.data

    print(data)
    course_id = data.get("course_id")
    nama = data.get("nama")
    description = data.get("description")

    if not (course_id and nama and description):
        response = {
            'status': 400,
            'message': 'Please provide course_id, nama, and description'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    course = Course.objects.create(course_id=course_id, nama=nama, description=description)
    course.save()

    response = {
        'status': 201,
        'messsage': 'Course created'
    }
    return Response(response, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def read(request, course_id):
    try:
        course = Course.objects.get(course_id=course_id)
    except Course.DoesNotExist:
        response = {
            'status': 400,
            'message': 'The course does not exist'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    response = {
        'status': 200,
        'course_id': course.course_id,
        'nama': course.nama,
        'description': course.description
    }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update(request, course_id):
    try:
        course = Course.objects.get(course_id=course_id)
    except Course.DoesNotExist:
        reponse = {
            'status': 400,
            'message': 'The course does not exist'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    try:
        data = json.loads(request.data.get('_content'))
    except TypeError:
        data = request.data
    if not (data.get("nama") or data.get("description")):
        response = {
            'status': 400,
            'message': 'Please provide the field you want to update'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    nama = data.get("nama", course.nama)
    description = data.get("description", course.description)

    course.nama = nama
    course.description = description
    course.save()

    response = {
        'status': 200,
        'message': 'The course has been updated'
    }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete(request, course_id):
    try:
        course = Course.objects.get(course_id=course_id)
    except Course.DoesNotExist:
        response = {
            'status': 400,
            'message': 'The course does not exist'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    course.delete()

    response = {
        'status': 200,
        'message': 'Course deleted'
    }
    return Response(response, status=status.HTTP_200_OK)
