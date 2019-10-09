# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 11:11 PM
# @Author  : all is well
# @File    : models.py
# @Software: PyCharm
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    """
    用户
    """
    real_name = models.CharField(max_length=50, verbose_name="姓名", default="")
    image = models.ImageField(upload_to="avatar/%Y/%m/%d", default=u"image/default.png", max_length=100,verbose_name="头像")
    roles = models.ManyToManyField(to='Role', verbose_name='角色')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Role(models.Model):
    """
    角色
    """
    name = models.CharField(max_length=32, unique=True, verbose_name="角色")
    permissions = models.ManyToManyField("Permission", blank=True, verbose_name="权限")
    desc = models.CharField(max_length=50, blank=True, null=True, verbose_name="描述")

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Permission(models.Model):
    """
    权限
    """
    name = models.CharField(max_length=32, unique=True,verbose_name="权限")
    path = models.CharField(max_length=128, unique=True, verbose_name="权限URL")
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标")
    component = models.CharField(max_length=200, null=True, blank=True, verbose_name="组件")
    menu = models.ForeignKey("Menu", null=True, blank=True, on_delete=models.SET_NULL, verbose_name='所属菜单')

    def __str__(self):
        # 显示带菜单前缀的权限
        return '{menu}---{permission}'.format(menu=self.menu, permission=self.name)

    class Meta:
        verbose_name = "权限"
        verbose_name_plural = verbose_name


class Menu(models.Model):
    """
    菜单
    """
    name = models.CharField(max_length=30, unique=True, verbose_name="菜单名")
    path = models.CharField(max_length=128, unique=True, verbose_name="菜单URL")
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标")
    hidden = models.BooleanField(default=False, verbose_name="隐藏菜单")
    component = models.CharField(max_length=200, null=True, blank=True, verbose_name="组件")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父菜单")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name
        ordering = ['id']

