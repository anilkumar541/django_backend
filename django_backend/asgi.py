
# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_backend.settings')

# application = get_asgi_application()


# ***************************************************

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
# from chat.routing import websocket_urlpatterns
import chat.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_backend.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns))
    # "websocket": AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(websocket_urlpatterns)))
    # Just HTTP for now. (We can add other protocols later.)
})