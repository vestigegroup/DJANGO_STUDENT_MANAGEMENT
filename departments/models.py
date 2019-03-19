from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30)
    dept_head = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

