from django.db import models


# Create your models here.


class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Roll = models.CharField(max_length=6)
    RegNo = models.CharField(max_length=6)
    ContactNo = models.CharField(max_length=11)
    ContactAddress = models.CharField(max_length=100)

    class Meta:
        db_table = "STUDENT"
