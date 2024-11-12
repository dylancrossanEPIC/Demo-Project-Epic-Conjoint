import json
from typing import List
from django.db import models
from django.core import serializers
from django.http import HttpResponse
from pydantic import TypeAdapter
from django.shortcuts import get_object_or_404
from ninja.responses import Response
from courses.schemas.courseSchema import CourseSchema


class Course(models.Model):
    course_title = models.CharField(max_length=200,default='')
    course_details = models.CharField(max_length=200,default='')
    course_pub_date = models.DateField()
    def __str__(self):
        return self.course_title, self.course_details, self.course_pub_date, self.id

