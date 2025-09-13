from django.urls import path
from .Consumers import NotificationConsumer

websocket_urlpatterns = [
    path("ws/notifications/" , NotificationConsumer.as_asgi())
]