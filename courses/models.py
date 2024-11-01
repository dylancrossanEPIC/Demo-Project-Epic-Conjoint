from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_length = models.IntegerField(default=0)


class Choice(models.Model):
    question = models.ForeignKey(Course, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)