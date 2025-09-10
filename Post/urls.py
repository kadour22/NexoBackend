from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/post/<int:id>/', views.PostRetrieveUpdateDestroyView.as_view(), name='posts'),
]
