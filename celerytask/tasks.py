#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from __future__ import absolute_import

import time
from datetime import timedelta

from celery.task import task, Task, PeriodicTask, periodic_task


class App01Task(Task):
    name = 'app01-task'

    def run(self, *args, **kwargs):
        print('task start')
        time.sleep(4)
        print('args{}\tkwargs{}'.format(args, kwargs))
        print('task finish')


class HeartBeat(PeriodicTask):
    name = 'heart_beat'
    run_every = timedelta(seconds=15)
    queue = "beat_queue"
    routing_key="beat.heart"

    def run(self, *args, **kwargs):
        task_data = {
            'ppt_id': 2295,
            'url': 'https://imglive.ehafo.com/course/temp/2019/04/3x1XfYGURwZsGtAB955Mq5fFypoLL39mCPOU2qfu.ppt',
            'course_root': None,
            'article_id': None,
        }
        return task_data


@periodic_task(run_every=timedelta(seconds=10))
def hello():
    return 'hello world'


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
