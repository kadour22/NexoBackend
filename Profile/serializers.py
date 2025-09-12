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
        
class UpdateProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name", required=False)
    last_name = serializers.CharField(source="user.last_name", required=False)

    class Meta:
        model = Profile
        fields = ["bio", "profile_image", "profile_cover", "first_name", "last_name"]

    def update(self, instance, validated_data):
        # Handle nested user data
        user_data = validated_data.pop("user", {})
        user = instance.user
        if "first_name" in user_data:
            user.first_name = user_data["first_name"]
        if "last_name" in user_data:
            user.last_name = user_data["last_name"]
        user.save()

        return super().update(instance, validated_data)
