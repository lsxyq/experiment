#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'id': user.id,
        'username': user.username,
        'token': token
    }
