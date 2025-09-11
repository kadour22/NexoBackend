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
        fields = ['id','username','posts','first_name', 'last_name']

class PostListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ["title", "author", "image", "created_at", "content", "likes", "likes_count"]
    def get_likes_count(self, obj):
        return obj.likes.count()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at","author","likes")
