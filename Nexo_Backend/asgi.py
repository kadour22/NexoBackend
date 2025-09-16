import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexo_Backend.settings')

django_application = get_asgi_application()

import Messages.routing
from Notification.middlewares import JWTAuthMiddleware
application = ProtocolTypeRouter({
    "http":get_asgi_application(),
     "websocket": AllowedHostsOriginValidator(
            JWTAuthMiddleware(
                URLRouter(Messages.routing.websocket_urlpatterns)
            )
        ),
})