from rest_framework import serializers
from .models import Comment


class CreateCommentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Comment
        fields= ["post","content","user"]
        read_only_fields = ["user"]


class ListCommentSerializer(serializers.ModelSerializer) :
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    # comments = ser
    class Meta :
        model = Comment
        fields= ["user","content","created_at","last_name","first_name","comments"]
