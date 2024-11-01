from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_course", views.create_course, name="create_course"),
    path("update_course", views.update_course, name="update_course"),
]