from django.db import models


class Course(models.Model):
    course_title = models.CharField(max_length=200,default='')
    course_details = models.CharField(max_length=200,default='')
    course_pub_date = models.DateField()
    def __str__(self):
        return self.course_title

    def getAllCourses():
        return Course.objects.all()
    
    def getCourseByID(course_id):
        try:
            course = Course.objects.get(pk=course_id)
            return 200, course
        except Course.DoesNotExist as e:
            return 404, {"message":"Course does not exist"}

    def createCourse(course):
        return Course.objects.create(**course.dict())

    def updateCourse(course_id, data):
        try:
            course = Course.objects.get(pk=course_id)
            for attribute, value in data.dict().items():
                setattr(course, attribute, value)
            course.save()
            return 200, course
        except Course.DoesNotExist as e:
            return 404, {"message":"Course does not exist"}
        
    def deleteCourse(course_id):
        try:
            course = Course.objects.get(pk=course_id)
            course.delete()
            return 200
        except Course.DoesNotExist as e:
            return 404, {"message": "Could not find course"}
