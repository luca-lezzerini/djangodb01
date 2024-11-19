from django.db import models


# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    studentID = models.IntegerField()


class Course(models.Model):
    title=models.CharField(max_length=255)
    code=models.CharField(max_length=10)
    credits = models.IntegerField()