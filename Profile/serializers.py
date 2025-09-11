from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from Post.serializers import PostListSerializer
    
class UserSerializer(serializers.ModelSerializer):
    posts = PostListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','posts']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'profile_image', 'profile_cover']