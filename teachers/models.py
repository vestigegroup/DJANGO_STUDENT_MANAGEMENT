from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    techer_id = models.CharField(unique=True, blank=True, null=True, max_length=6)
    #dept = models.ForeignKey('departments.Department', on_delete=models.CASCADE)
    designation = models.CharField(null=False, max_length=30)
    joined = models.DateField('Year-Month')
    phone = models.CharField(null=True, max_length=12)

    def __str__(self):
        return self.name
