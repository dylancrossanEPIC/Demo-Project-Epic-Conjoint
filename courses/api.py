from typing import List
from ninja import NinjaAPI
from courses.models import Course
from courses.schema import CourseSchema, NotFoundSchema

api = NinjaAPI()
@api.get("/courses", response=List[CourseSchema])
def test(request):
    return Course.objects.all()

