from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=0)
    course=models.CharField(max_length=100)
    mark=models.IntegerField(default=0)
    mobile = models.CharField(
    max_length=10,
    unique=True,
    validators=[RegexValidator(regex=r'^[69]\d{9}$',message='Mobile number must start with 6-9 and be exactly 10 digits')])
    email=models.EmailField(unique=True,validators=[RegexValidator(regex=r'^[a-zA-Z0-9._%+-]+@gmail\.com$',
                message='Email must contain @gmail.com')])
               




