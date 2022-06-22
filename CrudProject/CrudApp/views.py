from django.shortcuts import render, redirect

from .models import Student
from .forms import StudentForm


# Create your views here.


def show(request):
    students = Student.objects.all()
    return render(request, "show.html", {'students': students})


def saveStudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            pass
    else:
        form = StudentForm()
    return render(request, "save.html", {'form': form})


def deleteStudent(request, id):
    students = Student.objects.get(StudentID=id)
    students.delete()
    return redirect("/")


def editStudent(request, id):
    students = Student.objects.get(StudentID=id)
    return render(request, "edit.html", {'students': students})


def updateStudent(request, id):
    students = Student.objects.get(StudentID=id)
    form = StudentForm(request.POST, instance=students)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "edit.html", {'students': students})

