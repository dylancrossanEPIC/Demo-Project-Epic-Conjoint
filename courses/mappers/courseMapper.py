from typing import List
from courses.schemas.courseSchema import CourseSchema
from courses.models.courseModel import Course


class CourseMapper:

    def getAllCourses():
        return Course.objects.values('id', 'course_title', 'course_details', 'course_pub_date')

    
    def getCourseByID(course_id):
        try:
            course = Course.objects.get(pk=course_id)           
            pydantic_course = CourseSchema(
            id=course_id,
            course_title=course.course_title,
            course_details=course.course_details,
            course_pub_date=course.course_pub_date,
            )
            return 200, pydantic_course

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
            return 200, data
        except Course.DoesNotExist as e:
            return 404, {"message":"Course does not exist"}
        
    def deleteCourse(course_id):
        try:
            course = Course.objects.get(pk=course_id)
            course.delete()
            return 200
        except Course.DoesNotExist as e:
            return 404, {"message": "Could not find course"}
