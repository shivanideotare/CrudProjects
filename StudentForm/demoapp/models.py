from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length = 30)
    scity = models.CharField(max_length = 30)
    sid = models.IntegerField()

    def __str__(self):
        return self.sname
