import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = f"user_{self.scope['user'].id}"
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            print(f"User {self.scope['user'].username} connected to notifications")
            await self.accept()
  
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Called when we send a message to this user’s group
    async def send_notification(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
        }))
        print(f"{event['message']}")

