# -*- coding:utf-8 -*-
from django.urls import path
from apps.accounts.views import ListUsersView

app_name = 'accounts'

urlpatterns = [
    path('users/', ListUsersView.as_view(), name='users'),
]
