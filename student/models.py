from django.db import models
# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=None, null=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    gender = models.CharField(max_length=10)
    level = models.IntegerField()
    status = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name