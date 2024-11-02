from django.urls import path
from django.views.generic.base import TemplateView
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("create-course", views.create_course, name="create_course"),
    path("update-course", views.update_course, name="update_course"),
]