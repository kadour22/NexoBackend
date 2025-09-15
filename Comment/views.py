from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status

from .serializers import ListCommentSerializer , CreateCommentSerializer
from .models import Comment
from Post.models import Post


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

class CreateComment(generics.CreateAPIView) :
    serializer_class = CreateCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer) :
        return serializer.save(user=self.request.user)
