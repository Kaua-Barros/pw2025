import uuid

from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

# class Game(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
#     movie = models.ForeignKey(to=Movie, on_delete=models.SET_NULL)
#     alternatives = models.ManyToManyField(to=Movie)

#     choices = models.JSONField()
#     options = models.JSONField()

#     def save(self, *args, **kwargs):
#         if not self.uuid:
#             self.uuid = uuid.uuid4().hex 
#         super().save(*args, **kwargs)






