from rest_framework import serializers
from .models import Post
from User.serializers import UserSerializer
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at","author","likes")

class PostListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ["title", "author", "image", "created_at", "content", "likes"]