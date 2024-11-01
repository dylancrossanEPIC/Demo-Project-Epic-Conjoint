from typing import List
from ninja import NinjaAPI
from courses.models import Course
from courses.schema import CourseSchema, NotFoundSchema

api = NinjaAPI()
@api.get("/courses", response=List[CourseSchema])
def courses(request):
    return Course.objects.all()

@api.get("/courses/{course_id}", response={200: CourseSchema, 404: NotFoundSchema})
def course(request, course_id: int):
    try:
        course = Course.objects.get(pk=course_id)
        return 200, course
    except Course.DoesNotExist as e:
        return 404, {"message":"Course does not exist"}

@api.post("/courses", response={201: CourseSchema})
def createCourse(request, course: CourseSchema):
    course = Course.objects.create(**course.dict())
    return course

@api.put("/courses/{course_id}", response={200: CourseSchema, 404: NotFoundSchema})
def course(request, course_id: int, data: CourseSchema):
    try:
        course = Course.objects.get(pk=course_id)
        for attribute, value in data.dict().items():
            setattr(course, attribute, value)
        course.save()
        return 200, course
    except Course.DoesNotExist as e:
        return 404, {"message":"Course does not exist"}
