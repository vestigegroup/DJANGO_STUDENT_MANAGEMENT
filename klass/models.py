from django.db import models


class Klass(models.Model):
    grade = models.IntegerField(blank=False)
    guide = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)
    total_student = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.grade} | {self.guide}"
