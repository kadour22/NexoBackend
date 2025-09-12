from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model) :
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.content