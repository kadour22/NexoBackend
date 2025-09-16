from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms/<int:id>/', views.RoomDetailView.as_view(), name='room-detail'),
    path('messages/', views.MessageCreateView.as_view(), name='message-create'),
]
