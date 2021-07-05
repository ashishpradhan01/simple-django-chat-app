from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=10)
    datetime = models.DateTimeField(blank=True, default=timezone.now())

    # def __str__(self) -> str:
    #     return "Room Id: {}".format(self.name)

class Message(models.Model):
    username = models.CharField(max_length=10)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    date = models.DateTimeField(blank=True, default=timezone.now())
    createdAt = models.CharField(max_length=10, blank=True, default=str(datetime.now().strftime('%I:%M %p')))

    # def __str__(self) -> str:
    #     return "user: {} | {} | at: {}".format(self.username, self.room, self.createdAt)

