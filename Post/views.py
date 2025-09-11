from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .serializers import PostSerializer, PostListSerializer
from .models import Post

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostListView(generics.ListAPIView):
    queryset = Post.objects.select_related("author").all()
    serializer_class = PostListSerializer
    permission_classes = [permissions.AllowAny]

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.select_related("author").all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

class LikeOrDislikePost(APIView) :
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id) :
        user = request.user
        post = Post.objects.get(id=post_id)

        if user in post.likes.all() :
            post.likes.remove(user)
            return Response(f"{user.username} like post of {post.author}")
        else :
            post.likes.add(user)
            return Response(f"{user.username} remove like post of {post.author}")
