from django.db import models

# Create your models here.

class Course(models.Model):
    image=models.ImageField(upload_to="images") #pip install pillow
    title=models.CharField(max_length=20)
    desc=models.TextField()
    price=models.IntegerField()