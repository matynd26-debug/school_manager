from django.shortcuts import render
from django.http import Http404
from .models import Student
from django.shortcuts import get_object_or_404, render
STUDENTS = [
    {"id": 1, "first_name": "Awa", "last_name": "Diop", "classe": "L1", "active": True, "phone":"77 123 45 67"},
    {"id": 2, "first_name": "Moussa", "last_name": "Fall", "classe": "L2", "active": True, "phone":""},
    {"id": 3, "first_name": "Fatou", "last_name": "Ndiaye", "classe": "L1", "active": False, "phone": "77 862 49 10"},
    {"id": 4, "first_name": "Ibrahima", "last_name": "Sow", "classe": "L3", "active": True},#pas de téléphone du tout
]

TEACHERS = [
    {"first_name": "Mamadou", "last_name": "Ba", "subject": "Maths"},
    {"first_name": "Aissatou", "last_name": "Sy", "subject": "Français"},
]

def home(request):
    context = {
        "school_name": "Lycee d'Excellence de Dakar",
        "nb_classes": 12,
    }
    return render(request, "students/home.html", context)

def students_list(request):
    query = request.GET.get("q", "")
    students = Student.objects.all()
    if query:
        students = students.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    context = {"students": students, "query": query}
    return render(request, "students/students_list.html", context)

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    context = {"student": student}
    return render(request, "students/student_detail.html", context)

def teachers_list(request):
    return render(request, "students/teachers.html", {"teachers": TEACHERS})

def about(request):
    return render(request, "students/about.html")
def students_by_class(request, classe):
    students = Student.objects.filter(classe=classe)
    context = {"students": students}
    return render(request, "students/students_list.html", context)