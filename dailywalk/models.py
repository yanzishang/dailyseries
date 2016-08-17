from django.db import models

# Create your models here.


class Person (models.Model):

    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    date = models.DateTimeField()
    age = models.IntegerField()
