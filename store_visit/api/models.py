from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


class Store(models.Model):
    name = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Visit(models.Model):
    date_time = models.DateTimeField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
