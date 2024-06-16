from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    # re_path(r"ws/<str:room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),

]