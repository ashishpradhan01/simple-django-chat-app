from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=20,null=False)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "Room Id: {}".format(self.name)

class Message(models.Model):
    username = models.CharField(max_length=20, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages',null=False)
    message = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    createdAt = models.CharField(default=datetime.now().strftime('%I:%M %p'),null=False, max_length=255)

    def __str__(self) -> str:
        return "user: {} | {} | at: {}".format(self.username, self.room, self.createdAt)

