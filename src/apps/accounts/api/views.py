# -*- coding: utf-8 -*-
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.http import JsonResponse
from apps.accounts.api.serializers import UserSerializers


class ResultsSetPagination(PageNumberPagination):
    page_size = 5


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializers
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    pagination_class = ResultsSetPagination

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.serializer_class.data)
