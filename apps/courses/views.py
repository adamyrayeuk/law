from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course

@api_view(['POST'])
def create(request):
    course_id = request.data.get("course_id")
    nama = request.data.get("nama")
    description = request.data.get("description")

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
        course = Courses.objects.get(course_id=course_id)
    except Course.DoesNotExist:
        reponse = {
            'status': 400,
            'message': 'The course does not exist'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    if not (request.data.get("nama") or request.data.get("description")):
        response = {
            'status': 400,
            'message': 'Please provide the field you want to update'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    nama = request.data.get("nama", course.nama)
    description = request.data.get("description", course.description)

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