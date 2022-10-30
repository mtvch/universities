from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("universities/create/", views.university_create, name="university-create"),
    path(
        "universities/<int:university_id>/edit/",
        views.university_edit,
        name="university-edit",
    ),
    path(
        "universities/<int:university_id>/delete/",
        views.university_delete,
        name="university-delete",
    ),
    path("universities/<int:university_id>/", views.university, name="university"),
    path(
        "universities/<int:university_id>/student/<int:student_id>",
        views.student,
        name="student",
    ),
    path(
        "universities/<int:university_id>/student/create",
        views.student_create,
        name="student-create",
    ),
    path(
        "universities/<int:university_id>/student/<int:student_id>/edit",
        views.student_edit,
        name="student-edit",
    ),
    path(
        "universities/<int:university_id>/student/<int:student_id>/delete",
        views.student_delete,
        name="student-delete",
    ),
]
