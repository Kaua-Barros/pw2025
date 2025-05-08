from django.db import models

class Campus(models.Model):
    name = models.CharField(max_length=255)

class Game(models.Model):
    movie = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    choices = models.JSONField()
    options = models.JSONField()


