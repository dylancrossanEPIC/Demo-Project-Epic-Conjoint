from ninja import Router
from courses.models import Course
from courses.schema import CourseSchema, NotFoundSchema, CreateCourseSchema
from typing import List

auth_router = Router()
