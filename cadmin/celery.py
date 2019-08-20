#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from __future__ import absolute_import
import os
from celery import Celery, platforms

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cadmin.settings')

from django.conf import settings  # noqa

app = Celery('cadmin')
platforms.C_FORCE_ROOT = True  # 解决celery不能用root用户启动的问题

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)  # celery自动检索app是是否有tasks.py,有则自动创建任务


