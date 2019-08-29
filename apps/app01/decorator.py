#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from rest_framework.request import Request
from rest_framework.response import Response


def verify_status(action, key='pk', detail=False):
    def decorator(func):
        def inner(self, request: Request, *args, **kwargs):
            method = request.method
            if detail == True:
                pk = args[0]
            elif method.upper() == 'GET':
                pk = request.GET.get(key)
            elif method.upper() == 'POST':
                pk = request.data.get(key)
            elif method.upper() in ('DELETE', 'PUT'):
                lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
                pk = kwargs[lookup_url_kwarg]
            else:
                pk = None
            if pk is None:
                return Response({'info': '参数错误'})
            return func(self, request, *args, **kwargs)

        return inner

    return decorator
