from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name} - {self.code}"
