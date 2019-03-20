from django.db import models


class Klass(models.Model):
    grade = models.IntegerField(blank=False)
    #guide = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)
    total_student = models.IntegerField(null=True, default=0)

    def __str__(self):
        return str(self.grade)
