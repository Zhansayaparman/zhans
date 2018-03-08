from django.db import models
from django.contrib.auth.models import User
class Student(models.Model):
    ID = models.IntegerField(max_length=100)
    prepods = models.CharField(max_length=100)
    kafedras= models.CharField(max_length=100)
    bt_date = models.DateField()

    def __str__(self):
        return self.title


class Prepod(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)


class Kafedra(models.Model):
    name = models.CharField(max_length=30)
