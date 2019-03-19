from django.db import models


class Guardian(models.Model):
    name = models.CharField(max_length=50)
    #student_name = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    address = models.TextField(blank=False)
    phone = models.IntegerField(null=False)
    occopation = models.CharField(max_length=50)
    sex = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} -> {self.phone}"

