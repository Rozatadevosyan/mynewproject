import datetime

from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name



class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    salary = models.IntegerField()
    hire_date = models.DateField()
    department_id = models.ForeignKey(Department, on_delete=models.PROTECT)
    def __str__(self):
        return self.first_name + " " + self.last_name


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True)


    def __str__(self):
        return self.name

