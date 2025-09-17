import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AnonymousUser
from urllib.parse import parse_qs
from .models import Room, Message
from django.contrib.auth.models import User

# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        user = self.scope['user']

        room = await database_sync_to_async(Room.objects.get)(name=self.room_name)

        # Save message
        msg_obj = await database_sync_to_async(Message.objects.create)(
            room=room,
            user=user,
            content=message
        )

        payload = {
            "id": msg_obj.id,
            "content": msg_obj.content,
            "username": user.username if user.is_authenticated else "Anonymous",
            "timestamp": msg_obj.timestamp.isoformat(),
        }

        # Broadcast
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": payload,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event["message"]))


class TestingConsumer(AsyncWebsocketConsumer) :
    async def connect(self):
        user = self.scope["user"]
        if user.is_authenticated:
            await self.accept()
        else:
            await self.close()
            print("Anonymouse user")
    async def receive(self, text_data):
        user = self.scope["user"]
        await self.send(text_data=f"Hello {user.username}!")