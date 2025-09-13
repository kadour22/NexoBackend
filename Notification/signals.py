from .models import Notification
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save, sender=User)
def real_time_notifications(sender, instance, created, **kwargs) :
    if created :
        users = User.objects.all()
        # user = User.objects.get(instance.id)
        for user in users :
            notify = Notification.objects.create(
                user = user,
                message = f"{instance.username} Join Nexo Community"
            )
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "notifications",
                {
                    "type":"send_notification" , 
                    "message": notify.message
                }
            )