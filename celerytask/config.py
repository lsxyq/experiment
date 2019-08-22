#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from datetime import timedelta

import djcelery
from kombu import Queue

djcelery.setup_loader()

# 中间人，使用rabbitmq存储队列信息
BROKER_URL = 'amqp://127.0.0.1:5672'

# 将结果返回rabbitmq
RESULT_BACKEND = 'amqp://127.0.0.1:5672'

# 中间人，存储队列信息
# BROKER_URL = 'redis://:root@127.0.0.1:6379/0'

# 将结果返回到redis的1库
# CELERY_RESULT_BACKEND = 'redis://:root@localhost:6379/1'

# 如果开启，Celery便以eager模式运行, 则task便不需要加delay运行，记住没有加这个一定要再delay才是异步运行！！
# CELERY_ALWAYS_EAGER = True

# 时区设置
CELERY_TIMEZONE = 'Asia/Shanghai'

# 启动时区设置
CELERY_ENABLE_UTC = True

# 设置worker数量
CELERYD_CONCURRENCY = 10

# 每个worker最大执行次数
CELERYD_MAX_TASKS_PER_CHILD = 200

# 任务执行结果的超时时间
CELERY_TASK_RESULT_EXPIRES = 1200

# 单个任务的运行时间限制，否则会被杀死
CELERYD_TASK_TIME_LIMIT = 60

# 任务序列化方式
CELERY_TASK_SERIALIZER = 'pickle'

# 任务执行结果序列化方式
CELERY_RESULT_SERIALIZER = 'json'

# 队列的默认设置
CELERY_DEFAULT_QUEUE = "default"

CELERY_DEFAULT_EXCHANGE = 'tasks'

CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'

# CELERY_IMPORTS = (
#     "app01.tasks",
# )

# 队列的详细设置
CELERY_QUEUES = (  # 定义任务队列
    Queue("default", routing_key="default.#"),  # 路由键以“default.”开头的消息都进default队列
    Queue("beat_queue", routing_key="beat.#"),  # 路由键以“beat.”开头的消息都进beat_queue队列
    Queue("worker_queue", routing_key="worker.#"),  # 路由键以“worker.”开头的消息都进worker_queue队列
)

CELERY_ROUTES = {
    'app01.tasks.add':
        {
            'queue': 'beat_queue',
            'routing_key': "beat.add"
        },
    'app01-task':
        {
            'queue': 'worker_queue',
            'routing_key': "worker.task"
        },
    'app01.tasks.multiply':
        {
            'queue': 'default',
            'routing_key': "default.multiply"
        },
    'app01.tasks.test':
        {
            'queue': 'worker_queue',
            'routing_key': "worker.test"
        },
}

CELERYBEAT_SCHEDULE = {
    'add': {
        'task': 'app01.tasks.add',  # 运行定时任务test_celery, 要写路径中的tasks.py，必须为tasks.py文件
        'schedule': timedelta(seconds=3),  # 设置循环时间
        'args': (19, 16)  # 给定时任务的参数
    },
    'test': {
        'task': 'app01.tasks.test',  # 运行定时任务test_celery, 要写路径中的tasks.py，必须为tasks.py文件
        'schedule': timedelta(seconds=3),  # 设置循环时间
        'args': ('test task',)  # 给定时任务的参数
    },
}

# Celery通用配置
# CELERY_BROKER_URL
# BROKER_URL = 'redis://127.0.0.1:6379/0'
#
# # 指定结果的接收地址
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
#
# # 指定任务序列化方式
# CELERY_TASK_SERIALIZER = 'msgpack'
#
# # 指定结果序列化方式
# CELERY_RESULT_SERIALIZER = 'msgpack'
#
# # 指定任务接受的序列化类型.
# CELERY_ACCEPT_CONTENT = ['msgpack']
#
# # 任务过期时间，celery任务执行结果的超时时间
# CELERY_TASK_RESULT_EXPIRES = 24 * 60 * 60
#
# # 任务发送完成是否需要确认，对性能会稍有影响
# CELERY_ACKS_LATE = True
#
# # 压缩方案选择，可以是zlib, bzip2，默认是发送没有压缩的数据
# CELERY_MESSAGE_COMPRESSION = 'zlib'
#
# # 规定完成任务的时间
# # 在5s内完成任务，否则执行该任务的worker将被杀死，任务移交给父进程
# CELERYD_TASK_TIME_LIMIT = 5
#
# # celery worker的并发数，默认是服务器的内核数目,也是命令行-c参数指定的数目
# CELERYD_CONCURRENCY = 4
#
# # celery worker 每次去BROKER中预取任务的数量
# CELERYD_PREFETCH_MULTIPLIER = 4
#
# # 每个worker执行了多少任务就会死掉，默认是无限的
# CELERYD_MAX_TASKS_PER_CHILD = 40

# # 队列的详细设置
# CELERY_QUEUES = {
#     "default": {  # 这是上面指定的默认队列
#         "exchange": "default",
#         "exchange_type": "direct",
#         "routing_key": "default"
#     },
#     "topicqueue": {  # 这是一个topic队列 凡是topictest开头的routing key都会被放到这个队列
#         "routing_key": "topic.#",
#         "exchange": "topic_exchange",
#         "exchange_type": "topic",
#     },
#     "task_eeg": {  # 设置扇形交换机
#         "exchange": "tasks",
#         "exchange_type": "fanout",
#         "binding_key": "tasks",
#     },
# }
