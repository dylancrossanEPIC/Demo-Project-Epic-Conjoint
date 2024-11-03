from datetime import date
from ninja import Schema

class CourseSchema(Schema):
    id: int
    course_title: str
    course_details: str
    course_pub_date: date
    
class CreateCourseSchema(Schema):
    course_title: str
    course_details: str
    course_pub_date: date

class NotFoundSchema(Schema):
    message: str
    