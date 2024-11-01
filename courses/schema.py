from datetime import datetime
from ninja import Schema

class CourseSchema(Schema):
    course_title: str
    course_details: str
    course_pub_date: datetime

class NotFoundSchema(Schema):
    message: str