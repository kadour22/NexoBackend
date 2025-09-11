from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/post/<int:id>/', views.PostRetrieveUpdateDestroyView.as_view(), name='posts'),
    path("like_or_dislike/<int:post_id>", views.LikeOrDislikePost.as_view(), name='like_or_dislike')
]
