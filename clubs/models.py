from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    coach = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def short_desc(self):
        return self.description[:100]+'...'


class Activity(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    session_no = models.CharField(max_length=4)
    date = models.DateField()
    mentor = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.club)