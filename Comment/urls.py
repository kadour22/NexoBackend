from django.urls import path
from . import views

urlpatterns = [
    path("comments-list/<int:post_id>/", views.PostComments.as_view()),
    path("comments/<int:id>/", views.CreateComment.as_view()),
]
