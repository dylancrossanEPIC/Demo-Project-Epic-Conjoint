import datetime
from django.db import models


class Course(models.Model):
    course_title = models.CharField(max_length=200,default='')
    course_details = models.CharField(max_length=200,default='')
    course_pub_date = models.DateTimeField()