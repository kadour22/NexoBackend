from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"Notification for {self.user.username} at {self.timestamp}"


