from django.db import models
from django.utils import timezone

from shop.settings import AUTH_USER_MODEL


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.CharField(max_length=100000)
