#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from rest_framework.routers import DefaultRouter
from rest_framework.urls import urlpatterns

from app01.restful.cutomerviewset import CustomerViewSet
from app01.apps import App01Config
app_name = App01Config.name
router = DefaultRouter()
router.register('customer', CustomerViewSet, base_name='drf-customer')

urlpatterns += router.urls
