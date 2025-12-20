from django.db import models

# Create your models here.

class Course(models.Model):
    image=models.ImageField(upload_to="images") #pip install pillow
    title=models.CharField(max_length=20)
    desc=models.TextField()
    price=models.IntegerField()
    


class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    course=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    message=models.TextField()
    isdelete=models.BooleanField(default=False)
    
