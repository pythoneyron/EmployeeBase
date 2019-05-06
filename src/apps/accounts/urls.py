# -*- coding:utf-8 -*-
from django.urls import path
from apps.accounts.views import ListUsersView, LogoutFormView, DetaiUsersView

app_name = 'accounts'

urlpatterns = [
    path('user/<int:pk>/', DetaiUsersView.as_view(), name='detail'),
    path('users/', ListUsersView.as_view(), name='users'),
    path('users/alphabet/', ListUsersView.as_view(), name='users_alphabet'),
    path('logout/', LogoutFormView.as_view(), name='logout'),
]
