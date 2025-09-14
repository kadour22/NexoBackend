from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model) :
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    mark_as_read = models.BooleanField(default=False)

    def __str__(self) :
        return f"Notification for {self.message} at {self.timestamp}"


