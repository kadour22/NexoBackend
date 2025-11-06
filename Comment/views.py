from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.generics import GenericAPIView
from .serializers import ListCommentSerializer , CreateCommentSerializer
from .models import Comment
from Post.models import Post

from django.shortcuts import get_object_or_404

class PostComments(APIView):
    def get(self,request,post_id) :
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post)
        comments_count = comments.count()
        serializer = ListCommentSerializer(comments , many=True)
        return Response(
            {
                "data": serializer.data , 
                "count": comments_count 
            }, status=status.HTTP_200_OK
        )

class CreateComment(APIView) :
    def post(self, request, post_id) :
        serializer = CreateCommentSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)