from django.db import models
from datetime import date


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    techer_id = models.CharField(unique=True, max_length=6, null=True)
    designation = models.CharField(null=False, max_length=30)
    joined = models.DateField('Year-Month')
    phone = models.CharField(null=True, max_length=12)
       
    def __str__(self):
        return self.name


class TeacherInfo(models.Model):
    name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    gender = models.CharField(max_length=7)
    qualification = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    shortBio = models.CharField(max_length=85)
    email = models.EmailField(max_length=30)
    homeDistrict = models.CharField(max_length=20)
    currentLocation = models.CharField(max_length=80)
    description = models.TextField(max_length=400)

    def __str__(self):
        return str(self.name)


class EduLevel(models.Model):
    ''' This is to generate educational levels like
    ssc/hsc etc 
    '''
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    grade = models.CharField(max_length=15)
    yearCompleted = models.DateField()
    instituteName = models.CharField(max_length=100)

    def __str__(self):
        return self.grade


class TeacherQualification(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    level = models.ManyToManyField(EduLevel)

    def __str__(self):
        return str(self.teacher)

