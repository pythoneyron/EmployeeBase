# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings

from apps.accounts.models import User
from apps.accounts.api.serializers import UserSerializers


@receiver(post_save, sender=User)
def send_updated_users(sender, instance, created, **kwargs):
    serializer = UserSerializers(User.objects.all(), many=True)
    data = serializer.data
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(settings.GROUP_NAME_WEBSOCKET, {
        "type": "response.json",
        "updated_users": data,
    })
