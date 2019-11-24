# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 4:21 下午
# @Author  : all is well
# @File    : custom_pagination.py
# @Software: PyCharm

from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'size'
    page_query_param = 'page'

