from django.db import models


class Student(models.Model):
    client = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.client
