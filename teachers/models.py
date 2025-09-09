from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=20, unique=True)


    def __str__(self):
        return f"{self.name}  ({self.employee_id})"
# Create your models here.
