from django.db import models
from datetime import datetime

# Create your models here.

class Room(models.Model):
    name = models.CharField()
    datetime = models.DateTimeField(blank=True, default=datetime.now())

    def __str__(self) -> str:
        return "Room Id: {}".format(self.name)

class Message(models.Model):
    username = models.CharField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    message = models.CharField()
    date = models.CharField(blank=True, default=datetime.now().strftime('%d/%B/%Y'))
    createdAt = models.CharField(blank=True, default=datetime.now().strftime('%I:%M %p'))

    def __str__(self) -> str:
        return "user: {} | {} | at: {}".format(self.username, self.room, self.createdAt)

