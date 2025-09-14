from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth import get_user_model
from jwt import decode as jwt_decode, ExpiredSignatureError, DecodeError
from django.conf import settings

User = get_user_model()

@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()

class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query_string = parse_qs(scope["query_string"].decode())
        token = query_string.get("token")
        if token:
            try:
                # Validate token
                UntypedToken(token[0])
                # Decode token
                decoded_data = jwt_decode(token[0], settings.SECRET_KEY, algorithms=["HS256"])
                user_id = decoded_data.get("user_id")
                if user_id is None:
                    raise KeyError("user_id not in token")
                user = await get_user(user_id)
                scope["user"] = user
            except (InvalidToken, TokenError, ExpiredSignatureError, DecodeError, KeyError) as e:
                print("JWT auth failed:", e)
                scope["user"] = AnonymousUser()
        else:
            scope["user"] = AnonymousUser()
        return await super().__call__(scope, receive, send)
