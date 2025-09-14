from django.urls import re_path
from .Consumers import NotificationConsumer

websocket_urlpatterns = [
    re_path(r"ws/notifications/$" , NotificationConsumer.as_asgi())
]