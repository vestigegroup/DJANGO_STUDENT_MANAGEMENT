from django.db import models


class Guardian(models.Model):
    name = models.CharField(max_length=50)
    #student_name = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    address = models.TextField(blank=False)
    phone = models.CharField(null=False, max_length=11)
    occopation = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)     # Use M/F for gender

    def __str__(self):
        return f"{self.name} -> {self.phone}"

