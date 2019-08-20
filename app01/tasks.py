#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x

from __future__ import absolute_import

import time

from celery import task


@task
def test_celery(x, y):  # 创建的任务，在setting中应用，作为定时任务
    print(x + y)
    return x + y  # 在setting中设置了CELERY_RESULT_BACKEND所有把结果返回到redis中去


@task
def test_multiply(x, y):
    time.sleep(10)  # 模拟耗时操作
    print(x * y)
    return x * y
