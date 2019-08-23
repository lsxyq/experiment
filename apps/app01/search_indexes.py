#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x

import datetime

from app01.models import Customer
from haystack import indexes


class CustomerIndex(indexes.SearchIndex, indexes.Indexable):  # 类名必须为需要检索的Model_name+Index，这里需要检索Note，所以创建NoteIndex
    text = indexes.CharField(document=True, use_template=True)  # 创建一个text字段
    phone = indexes.CharField(model_attr='phone')  # 创建一个author字段
    name = indexes.CharField(model_attr='name')  # 创建一个author字段
    time_create = indexes.DateTimeField(model_attr='time_create')  # 创建一个pub_date字段

    def get_model(self):  # 重载get_model方法，必须要有！
        return Customer
