from ninja import Router
from courses.models.courseModel import Course
from courses.schemas.courseSchema import CourseSchema, NotFoundSchema, CreateCourseSchema
from typing import List

course_router = Router()

@course_router.get("", response=List[CourseSchema])
def courses(request):
    return Course.getAllCourses()

@course_router.get("/{course_id}", response={200: CourseSchema, 404: NotFoundSchema})
def course(request, course_id: int):
    return Course.getCourseByID(course_id)

@course_router.post("", response={201: CreateCourseSchema})
def create_course(request, course: CreateCourseSchema):
    return Course.createCourse(course)

@course_router.put("/{course_id}", response={200: CourseSchema, 404: NotFoundSchema})
def update_course(request, course_id: int, data: CourseSchema):
    return Course.updateCourse(course_id, data)

@course_router.delete("/{course_id}", response={200: None, 404: NotFoundSchema})
def delete_course(request, course_id: int):
    return Course.deleteCourse(course_id)