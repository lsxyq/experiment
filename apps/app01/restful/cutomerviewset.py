#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from app01.models import Customer
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication



class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        return res
