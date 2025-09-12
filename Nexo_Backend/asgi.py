import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexo_Backend.settings')

django_application = get_asgi_application()

from Middlewares import JWTAuthMiddleware
import Notification.routing
application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket": URLRouter(
        Notification.routing.websocket_urlpatterns
    )
})