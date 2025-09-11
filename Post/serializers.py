from rest_framework import serializers
from .models import Post
# from Profile.serializers import 
from django.contrib.auth.models import User


class PostListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at","author","likes")

class UserSerializer(serializers.ModelSerializer):
    posts = PostListsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username','posts']

class PostListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ["title", "author", "image", "created_at", "content", "likes"]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at","author","likes")
