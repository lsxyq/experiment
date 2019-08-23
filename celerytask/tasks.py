#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from __future__ import absolute_import

import time

from celery.task import task, Task


class App01Task(Task):
    name = 'app01-task'

    def run(self, *args, **kwargs):
        print('task start')
        time.sleep(4)
        print('args{}\tkwargs{}'.format(args, kwargs))
        print('task finish')


@task
def test(info):
    time.sleep(10)  # 模拟耗时操作
    print(5 * 4)
    return {'code': 0, 'info': info}


@task
def multiply():
    time.sleep(10)  # 模拟耗时操作
    print(5 * 4)
    return 5 * 4


@task
def add(x, y):  # 创建的任务，在setting中应用，作为定时任务
    print(x + y)
    return x + y  # 在setting中设置了CELERY_RESULT_BACKEND所有把结果返回到redis中去



