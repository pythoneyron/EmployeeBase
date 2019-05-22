# -*- coding: utf-8 -*-
from django.urls import path

from apps.accounts.consumers import UsersConsumer

websocket_urlpatterns = [
    path('ws/users/', UsersConsumer),
]
