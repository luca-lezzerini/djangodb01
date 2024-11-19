from django.http import HttpResponse
from django.shortcuts import render

from dbexample.models import Student


# Create your views here.
def addstudent(request):
    s = Student(firstname="Ledio",lastname="Hoxha",studentID=1000)
    s.save()
    res = Student.objects.all().values()
    print(res)
    todelete = Student.objects.all()[0]
    todelete.delete()
    res2 = Student.objects.all().values()
    print(res2)
    return HttpResponse(res2)