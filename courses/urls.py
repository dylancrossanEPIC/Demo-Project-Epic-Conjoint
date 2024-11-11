from django.urls import path
from . import views
from courses.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("createcourse", views.create_course, name="create_course"),
    path("updatecourse/<int:id>", views.update_course, name="update_course"),
    path("courses/<int:id>/", views.delete_course, name="delete_course"),
]