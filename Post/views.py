from rest_framework import generics, permissions
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