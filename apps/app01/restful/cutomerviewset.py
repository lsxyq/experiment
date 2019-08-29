#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from app01.models import Customer
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.app01.decorator import verify_status


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomSerializer

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        return res

    @verify_status(action='post')
    def create(self, request, *args, **kwargs):
        res = super().create(request, *args, **kwargs)
        return res

    @verify_status(action='put')
    def update(self, request, *args, **kwargs):
        res = super().update(request, *args, **kwargs)
        return res

    @action(methods=['get', ], detail=False)
    def test(self, request):
        return self.test_action(request)

    @verify_status(action='ssd', key='pk')
    def test_action(self, request):
        pk = request.GET.get('pk')
        instance = self.queryset.get(id=pk)
        data = self.get_serializer(instance).data
        return Response(data)
