from django.shortcuts import render

from students.models import Student
from teachers.models import Teacher


def home(request):
    context = {
        "school_name": "Lycée d'Excellence de Dakar",
        "nb_students": Student.objects.count(),
        "nb_active": Student.objects.filter(active=True).count(),
        "nb_teachers": Teacher.objects.count(),
    }
    return render(request, "pages/home.html", context)


def about(request):
    return render(request, "pages/about.html")