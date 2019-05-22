# -*- coding: utf-8 -*-
from rest_framework import serializers

from apps.accounts.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'get_full_name', 'get_age', 'get_company', 'position',
                  'get_section', 'start_date', 'end_date', 'get_status')
