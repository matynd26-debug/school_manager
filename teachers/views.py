from django.shortcuts import render

TEACHERS = [
    {"first_name": "Mamadou", "last_name": "Ba", "subject": "Mathématiques" ,"email":"mamadou.ba@ecole.sn"},
    {"first_name": "Aïssatou", "last_name": "Sy", "subject": "Informatique","email":"aissatou.sy@ecole.sn"},
    {"first_name": "Cheikh", "last_name": "Diallo", "subject": "Anglais","email":"cheikh.diallo@ecole.sn"},
]


def teacher_list(request):
    context = {"teachers": TEACHERS}
    return render(request, "teachers/teacher_list.html", context)
    