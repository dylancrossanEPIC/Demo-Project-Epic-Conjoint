from datetime import date
from ninja import Schema

class CourseSchema(Schema):
    course_title: str
    course_details: str
    course_pub_date: date

class NotFoundSchema(Schema):
    message: str