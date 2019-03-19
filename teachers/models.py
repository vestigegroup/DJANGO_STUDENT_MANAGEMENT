from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    techer_id = models.IntegerField(blank=False)
    #dept = models.ForeignKey('departments.Department', on_delete=models.CASCADE)
    designation = models.CharField(null=False, max_length=30)
    joined = models.DateField('Year-Month')
    phone = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
