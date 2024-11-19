from django.shortcuts import render

from dbexample.models import Student


# Create your views here.
def addstudent(request):
    s = Student(firstname="Ledio",lastname="Hoxha",studentID=1000)
    s.save()