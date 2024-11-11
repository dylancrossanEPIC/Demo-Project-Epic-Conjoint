import json
from ninja import Router
from courses.mappers.courseMapper import CourseMapper
from courses.schemas.courseSchema import CourseSchema, NotFoundSchema, CreateCourseSchema
from typing import List

course_router = Router()
    

class CourseAPI:

    @course_router.get("", response=List[CourseSchema])
    def courses(request):
        courses = CourseMapper.getAllCourses()
        return [CourseSchema(**course) for course in courses]


    @course_router.get("/{course_id}", response={200: CourseSchema, 404: NotFoundSchema})
    def course(request, course_id: int):
        course = CourseMapper.getCourseByID(course_id)
        return course


    @course_router.post("", response={201: CreateCourseSchema})
    def create_course(request, course: CreateCourseSchema):
        return CourseMapper.createCourse(course)

    @course_router.put("/{course_id}", response={200: CourseSchema, 404: NotFoundSchema})
    def update_course(request, course_id: int, data: CourseSchema):
        return CourseMapper.updateCourse(course_id, data)

    @course_router.delete("/{course_id}", response={200: None, 404: NotFoundSchema})
    def delete_course(request, course_id: int):
        return CourseMapper.deleteCourse(course_id)