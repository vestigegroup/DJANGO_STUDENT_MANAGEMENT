from django.db import models
from datetime import date


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    techer_id = models.CharField(unique=True, blank=True, null=True, max_length=6)
    designation = models.CharField(null=False, max_length=30)
    joined = models.DateField('Year-Month')
    phone = models.CharField(null=True, max_length=12)
    def __str__(self):
        return self.name


class TeacherDetail(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    dept = models.ForeignKey('departments.Department', on_delete=models.CASCADE)
    short_bio = models.TextField(max_length=100)
    gender = models.CharField(max_length=6)
    birthdate = models.DateField()
    qualification = models.CharField(max_length=100)
    englis_skill = models.CharField(max_length=10)
    math_skill = models.CharField(max_length=10, blank=True, null=True)
    programming_skill = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.teacher)

    def age(self, dob):
        dob = self.birthdate
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    

