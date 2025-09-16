from django.db import models
from django.contrib.auth.models import User

class Post(models.Model) :
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE , related_name="posts")
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User)

    def __str__(self):
        return self.title
    
    def count_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created_at']

        indexes = [
            models.Index(fields=['id', 'author']),
        ]