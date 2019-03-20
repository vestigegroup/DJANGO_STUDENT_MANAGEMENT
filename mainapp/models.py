from django.db import models


class Meeting(models.Model):
    date = models.DateTimeField('Time')

    def __str__(self):
        return str(self.date)


class ToDo(models.Model):
    todo = models.CharField(max_length=300)
    todo_time = models.DateTimeField('Time')

    def __str__(self):
        return f"{self.todo} -- {self.todo_time}"


class EventGallery(models.Model):
    name = models.CharField(max_length=25)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media')
    date = models.DateTimeField('Time')

    def __str__(self):
        return f"{self.name} | {self.country} | {self.city} | {str(self.date)}"

