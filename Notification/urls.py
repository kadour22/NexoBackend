from django.urls import path
from . import views

urlpatterns = [
    path("notifications/", views.NotificationsList.as_view())
]