from django.db.models import Prefetch
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student, University


def index(request):
    universities = University.objects.order_by("-id")
    context = {"universities": universities}
    return render(request, "index.html", context)


def university(request, university_id):
    try:
        current_university = University.objects.prefetch_related(
            Prefetch("student_set", queryset=Student.objects.order_by("-id"))
        ).get(id=university_id)
    except University.DoesNotExist:
        raise Http404("University does not exist")
    context = {"university": current_university}
    return render(request, "university.html", context)


def university_create(request):
    if request.method == "GET":
        return render(request, "university/createform.html")
    if request.method == "POST":
        full_name = request.POST["full_name"]
        short_name = request.POST["short_name"]
        created_at = request.POST["created_at"]
        University(
            full_name=full_name, short_name=short_name, created_at_date=created_at
        ).save()
        return HttpResponseRedirect(reverse("index"))
    return Http404()


def university_edit(request, university_id):
    if request.method == "GET":
        university_to_edit = University.objects.get(pk=university_id)
        return render(
            request, "university/editform.html", {"university": university_to_edit}
        )
    if request.method == "POST":
        full_name = request.POST["full_name"]
        short_name = request.POST["short_name"]
        created_at = request.POST["created_at"]
        University.objects.filter(pk=university_id).update(
            full_name=full_name, short_name=short_name, created_at_date=created_at
        )
        return HttpResponseRedirect(reverse("university", args=(university_id,)))
    return Http404()


def university_delete(request, university_id):
    if request.method == "POST":
        University.objects.filter(pk=university_id).delete()
        return HttpResponseRedirect(reverse("index"))
    return Http404()


def student(request, university_id, student_id):
    try:
        current_student = Student.objects.select_related("university").get(
            id=student_id
        )
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    context = {"student": current_student}
    return render(request, "student.html", context)


def student_create(request, university_id):
    if request.method == "GET":
        return render(
            request, "student/createform.html", {"university_id": university_id}
        )
    if request.method == "POST":
        full_name = request.POST["full_name"]
        birth_date = request.POST["birth_date"]
        year_entered = request.POST["year_entered"]
        Student(
            full_name=full_name,
            birth_date=birth_date,
            year_entered=year_entered,
            university_id=university_id,
        ).save()
        return HttpResponseRedirect(reverse("university", args=(university_id,)))
    return Http404()


def student_edit(request, university_id, student_id):
    if request.method == "GET":
        student_to_edit = Student.objects.get(pk=student_id)
        universities = University.objects.order_by("short_name").all()
        return render(
            request,
            "student/editform.html",
            {"student": student_to_edit, "universities": universities},
        )
    if request.method == "POST":
        print(request)
        full_name = request.POST["full_name"]
        birth_date = request.POST["birth_date"]
        year_entered = request.POST["year_entered"]
        university_id = request.POST["university_id"]
        Student.objects.filter(pk=student_id).update(
            full_name=full_name,
            birth_date=birth_date,
            year_entered=year_entered,
            university_id=university_id,
        )
        return HttpResponseRedirect(
            reverse(
                "student",
                args=(
                    university_id,
                    student_id,
                ),
            )
        )
    return Http404()


def student_delete(request, university_id, student_id):
    if request.method == "POST":
        Student.objects.filter(pk=student_id).delete()
        return HttpResponseRedirect(reverse("index"))
    return Http404()
