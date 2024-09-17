from django.db import models

# Create your models here.
class Company(models.Model):
    compmpany_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Location = models.CharField(max_length=100)
    Description = models.TextField()
    Type = models.CharField(max_length=100,choices=(("IT","IT"),("Banking","Banking"),("Services","Services")))
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.Name
class Employee(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Salary = models.IntegerField()
    position = models.CharField(max_length=100,choices=(
        ("SoftWare Developer","SoftWare Developer"),
        ("Accounts","Accounts"),
        ("Sales","Sales"),
        ("Manager","Manager"),
        ("Project Manager","Project Manager"),
        ("Team Leader","Team Leader"),
        ))
    Company = models.ForeignKey(Company,on_delete=models.CASCADE)