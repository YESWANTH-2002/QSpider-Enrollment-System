# enrollment/models.py
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    selected_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    has_paid_fees = models.BooleanField(default=False)
