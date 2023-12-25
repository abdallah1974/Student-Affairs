from django.db import models

# Create your models here.
class Signin(models.Model):
    id = models.IntegerField(primary_key=True)
    Fname = models.CharField(max_length=100, null=True, default=None)
    Lname = models.CharField(max_length=100, null=True, default=None)
    date = models.DateField(default=None, null=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=None, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')] , default=None, null=True)
    level = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1 , null = True)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')], default=None,null=True)
    email = models.EmailField(default=None,null=True)
    phone = models.CharField(max_length=11, default=None,null=True)
    dep = models.CharField(max_length=50, choices=[('General', 'General'), ('CS', 'CS'), ('IT', 'IT'), ('DS', 'DS'), ('IS', 'IS'), ('AI', 'AI')], default=None,null = True)