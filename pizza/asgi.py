"""
ASGI config for pizza project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import django
django.setup()
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizza.settings')
from django.urls import path
from home.consumer import OrderProgress


django_asgi_app = get_asgi_application()
ws_pattern=[path("ws/pizza/<order_id>/", OrderProgress.as_asgi()),]
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': URLRouter(ws_pattern)
    # Just HTTP for now. (We can add other protocols later.)
})