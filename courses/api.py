from ninja import NinjaAPI
from courses.routers.coursesRouter import course_router

api = NinjaAPI()

api.add_router("/courses", course_router)