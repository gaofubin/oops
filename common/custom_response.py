#!/usr/bin env python
# -*- coding: utf-8 -*-
# @Time        : 2019/12/6 21:31
# @Author      : All is well
# @File        : custom_response.py
# @Software    : PyCharm

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class ReturnFormat:
    def __init__(self, response, errors=None, code=None):
        self.data = [] if not response.data else response.data
        self.code = [] if not response.status_code else response.status_code
        self.errors = {} if errors is None else errors

    def dict(self):
        return {
            'meta': {
                'code': self.code,
                'errors': self.errors
            },
            'data': self.data
        }


class CustomModelViewSet(ModelViewSet):
    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        return Response(ReturnFormat(response=response).dict())

    def create(self, request, *args, **kwargs):
        response = super().create(request, args, kwargs)
        return Response(ReturnFormat(response=response).dict())

    def update(self, request, *args, **kwargs):
        response = super().update(request, args, kwargs)
        return Response(ReturnFormat(response=response).dict())

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, args, kwargs)
        return Response(ReturnFormat(response=response).dict())

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, args, kwargs)
        return Response(ReturnFormat(response=response).dict())