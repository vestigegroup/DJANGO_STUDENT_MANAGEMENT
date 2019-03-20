from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    roll = models.IntegerField(null=False)
    registration = models.IntegerField(null=False)
    phone = models.CharField(null=True, max_length=11)
    session_start = models.DateField(verbose_name=u"Session start")
    session_end = models.DateField(verbose_name=u"Session start")
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE)
    klass = models.ForeignKey('klass.Klass', on_delete=models.CASCADE)
    parent = models.ForeignKey('parents.Guardian', on_delete=models.CASCADE)

    def session(self, start, end):
        self.start = session_start
        self.end = session_end
        return f"{self.start} to {self.end}"
    
    def __str__(self):
        return f"{self.name} | {self.klass} | {self.department}"

