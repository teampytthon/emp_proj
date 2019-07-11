from django.db import models
from django.urls import reverse

class Department(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return  self.dept_name

    def get_absolute_url(self):
        return  reverse('department:index')


class Employee(models.Model):
    dep_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return (self.first_name+" "+self.last_name)


