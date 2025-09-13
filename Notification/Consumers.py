from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AnonymousUser
from urllib.parse import parse_qs
import json

class NotificationConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("🔌 WebSocket connect called")
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()
        print("✅ WebSocket connected")

    async def disconnect(self, close_code):
        print(f"❌ WebSocket disconnected: {close_code}")
        await self.channel_layer.group_discard("notifications", self.channel_name)

    async def send_notification(self, event):
        message = event["message"]
        print(f"📨 Sending notification: {message}")
        await self.send(text_data=json.dumps({
            "type": "notification",
            "message": message
        }))
    
    # --------- Helpers ---------
    @database_sync_to_async
    def get_user_from_token(self, token):
        if not token:
            return AnonymousUser()
        jwt_auth = JWTAuthentication()
        try:
            validated_token = jwt_auth.get_validated_token(token)
            user = jwt_auth.get_user(validated_token)
            return user
        except Exception:
            return AnonymousUser()