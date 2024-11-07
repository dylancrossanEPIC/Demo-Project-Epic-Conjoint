from ninja import NinjaAPI
from courses.routers.coursesRouter import course_router
from courses.routers.authRouter import auth_router

api = NinjaAPI()

api.add_router("/courses", course_router)
api.add_router("/auth", auth_router)