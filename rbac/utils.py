#!/usr/bin env python
# -*- coding: utf-8 -*-
# @Time        : 2019/9/7 10:27
# @Author      : All is well
# @File        : utils.py
# @Software    : PyCharm
from rest_framework.views import Response
from rest_framework.serializers import Serializer
from rest_framework import status


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    data = {
        'token': token
    }
    return data


class OopsResponse(Response):
    def __init__(self, data=None, status=None, msg='成功',
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        """
            继承Response，把data封装code与msg参数
        """
        super().__init__(None, status=status)

        if isinstance(data, Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)

        if status >= 400:
            msg = '失败'
        self.data = {
            'code': status,
            'message': msg,
            'detail': data
        }

        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in headers.items():
                self[name] = value