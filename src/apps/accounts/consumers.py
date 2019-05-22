# -*- coding: utf-8 -*-
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.core.paginator import Paginator
from django.conf import settings

from apps.accounts.utils import query_filter_users
from apps.accounts.models import User
from apps.accounts.api.serializers import UserSerializers


class UsersConsumer(AsyncJsonWebsocketConsumer):
    # users_paginate = Paginator(User.objects.all(), 5)

    async def connect(self):
        await self.channel_layer.group_add(settings.GROUP_NAME_WEBSOCKET, self.channel_name)
        await self.accept()
        await self.send_json({'connected': 'WebSocket connected'})
        await self.send_json({'users_json': UserSerializers(User.objects.all().order_by('-id'), many=True).data})

    async def disconnect(self, code):
        await self.channel_layer.group_discard(settings.GROUP_NAME_WEBSOCKET, self.channel_name)
        await self.close()

    async def receive_json(self, content, **kwargs):
        if 'get_users_alphabet' in content:
            range_alphabet = content['get_users_alphabet'].get('range_alphabet')
            if range_alphabet:
                query = query_filter_users(range_alphabet)
                users_alphabet = UserSerializers(User.objects.filter(query).order_by('-id'), many=True).data
            else:
                users_alphabet = UserSerializers(User.objects.all().order_by('-id'), many=True).data
            message = {
                'type': 'response.json',
                'users_alphabet': users_alphabet,
            }
            await self.channel_layer.group_send(settings.GROUP_NAME_WEBSOCKET, message)

    async def response_json(self, content):
        await self.send_json(content)
