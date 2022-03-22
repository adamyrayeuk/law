from django.db import models

class Course(models.Model):
    course_id = models.CharField(unique=True, max_length=10)
    nama = models.CharField(max_length=255)
    description = models.TextField()