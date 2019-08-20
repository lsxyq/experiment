#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from import_export import resources

from app01.models import Customer


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'type', 'company_code', 'time_create')
