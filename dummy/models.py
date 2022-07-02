from django.db import models


class Ci(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()


class CD(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
