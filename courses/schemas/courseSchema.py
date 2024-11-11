from datetime import date
from pydantic import BaseModel

class CourseSchema(BaseModel):
    id: int
    course_title: str
    course_details: str
    course_pub_date: date
 
    
class CreateCourseSchema(BaseModel):
    course_title: str
    course_details: str
    course_pub_date: date

class NotFoundSchema(BaseModel):
    message: str