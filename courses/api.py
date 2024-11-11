from ninja import NinjaAPI
from courses.routers.coursesRouter import course_router
from ninja_extra import NinjaExtraAPI


api = NinjaAPI(version="1.0.0")

api.add_router("/courses", course_router)


