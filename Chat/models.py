from django.db import models
from Account.models import User


class Room(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name ="reciver")

    def __str__(self):
        return f"{self.sender.username}: {self.text} ({self.created_at})"