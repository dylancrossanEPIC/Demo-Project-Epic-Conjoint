from typing import List
from ninja import NinjaAPI
from courses.models import Course
from courses.schema import CourseSchema, NotFoundSchema, CreateCourseSchema

api = NinjaAPI()
@api.get("/courses", response=List[CourseSchema])
def courses(request):
    return Course.getAllCourses()

@api.get("/courses/{course_id}", response={200: CourseSchema, 404: NotFoundSchema})
def course(request, course_id: int):
    return Course.getCourseByID(course_id)

@api.post("/courses", response={201: CreateCourseSchema})
def create_course(request, course: CreateCourseSchema):
    return Course.createCourse(course)

@api.put("/courses/{course_id}", response={200: CourseSchema, 404: NotFoundSchema})
def update_course(request, course_id: int, data: CourseSchema):
    return Course.updateCourse(course_id, data)

@api.delete("/courses/{course_id}", response={200: None, 404: NotFoundSchema})
def delete_course(request, course_id: int):
    return Course.deleteCourse(course_id)