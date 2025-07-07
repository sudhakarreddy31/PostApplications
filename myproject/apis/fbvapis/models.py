from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male','Male'),('Female','Female'),('Other','Other')])
    enrollment_date = models.DateField(auto_now_add=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
    