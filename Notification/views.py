from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import NotificationSerializer
from .models import Notification

class NotificationsList(APIView) :
    def get(self , request) :
        notifications = Notification.objects.select_related("user").all()
        notifications_count = notifications.count()
        serializer = NotificationSerializer(notifications, many=True)
        return Response({
            "count": notifications_count,
            "notifications": serializer.data
        }, status=status.HTTP_200_OK)