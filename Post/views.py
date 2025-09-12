from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .serializers import PostSerializer, PostListSerializer , ActiveUserSerializer
from .models import Post

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self,serializer) :
        return serializer.save(author=self.request.user)

class PostListView(generics.ListAPIView):
    queryset = Post.objects.select_related("author").all()
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.select_related("author").all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

class LikeOrDislikePost(APIView) :
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id) :
        user = request.user
        serializer = ActiveUserSerializer(user)
        post = Post.objects.get(id=id)

        if user in post.likes.all() :
            post.likes.remove(user)
            return Response(
                {
                    "user_id":serializer.data
                }, status=201
            )
        else :
            post.likes.add(user)
            return Response(
                {
                    "user_id":serializer.data
                }, 
            )
class ActiveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = ActiveUserSerializer(user)
        return Response(serializer.data)