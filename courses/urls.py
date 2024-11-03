from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createcourse", views.create_course, name="create_course"),
    path("updatecourse", views.update_course, name="update_course"),
]