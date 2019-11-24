# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 2:04 下午
# @Author  : all is well
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, re_path, include
from rbac import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers

router = routers.SimpleRouter()
router.register('users', views.UserViewSet, base_name='users')

urlpatterns = [
    path(r'api/', include(router.urls)),
    path('auth/login', obtain_jwt_token),
    path('auth/info', views.UserInfoView.as_view()),

]
