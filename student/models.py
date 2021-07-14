from django.db import models
from django.db.models.fields import CharField
# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    lab=models.CharField(max_length=9)
    nationality=models.CharField(max_length=13)
    identification=models.CharField(max_length=20)
