from django.db import models

# Create your models here.
class  teacher(models.Model):

    fname=models.CharField(max_length=40)
    lname=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    def __str__(self):
        return self.fname
class student(models.Model):
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)